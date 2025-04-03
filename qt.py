import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')

def init():
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    return line,

def update(frame):
    x, y = line.get_data()
    x = np.append(x, frame)
    y = np.append(y, np.sin(frame))
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), init_func=init, blit=True)
while True:
    plt.show()
    plt.pause(0.1)  # Небольшая пауза перед следующей итерацией
    x.append(np.pi)