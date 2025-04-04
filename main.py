import threading
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import time

# Настройки serial порта (замените на свои)
SERIAL_PORT = 'COM3'  # или '/dev/ttyUSB0' для Linux
BAUD_RATE = 9600

# Глобальные переменные для обмена между потоками
data_buffer = deque(maxlen=100)  # Ограничиваем размер буфера для эффективности
lock = threading.Lock()
stop_threads = False


# Функция для чтения данных с serial порта
def serial_reader():
    global data_buffer, stop_threads

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Подключено к {SERIAL_PORT} на {BAUD_RATE} бод")

        while not stop_threads:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    try:
                        value = int(line)
                        print(value)
                        with lock:
                            data_buffer.append(value)
                    except ValueError:
                        print(f"Неверные данные: {line}")
            except UnicodeDecodeError:
                print("Ошибка декодирования данных")

        ser.close()
        print("Подключение завершено")
    except serial.SerialException as e:
        print(f"Ошибка serial порта: {e}")
        stop_threads = True


# Функция для обновления графика
def update_plot(frame):
    print("График обновлен")
    with lock:
        if data_buffer:
            print(data_buffer)

            line.set_data(range(len(data_buffer)), data_buffer)
            ax.relim()
            ax.autoscale_view()
    return line


# Функция для закрытия окна
def on_close(event):
    global stop_threads
    stop_threads = True


# Создаем график
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-')
ax.set_title('Real-time Serial Data')
ax.set_xlabel('Time')
ax.set_ylabel('Value')
fig.canvas.mpl_connect('close_event', on_close)

# Запускаем поток для чтения serial данных
serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

# Настраиваем анимацию для обновления графика
ani = FuncAnimation(fig, update_plot, interval=1, blit=False)

plt.show()

# После закрытия окна
stop_threads = True
serial_thread.join()
print("Программа завершена")