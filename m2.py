# server.py
from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Генерация начальных данных
data = [{
    'x': [],
    'y': [],
    'type': 'scatter'
}]

def generate_data():
    while True:
        # Добавляем новые данные каждую секунду
        data[0]['x'].append(time.strftime('%H:%M:%S'))
        data[0]['y'].append(random.randint(1, 100))
        # Сохраняем только последние 20 точек
        if len(data[0]['x']) > 20:
            data[0]['x'] = data[0]['x'][-20:]
            data[0]['y'] = data[0]['y'][-20:]
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    # Запускаем генератор данных в отдельном потоке
    import threading
    threading.Thread(target=generate_data, daemon=True).start()
    app.run(debug=True)