def addData():
    x.a

import pygame
from pygame.locals import OPENGL
import numpy as np
import time
import threading

pygame.init()
WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

font = pygame.font.SysFont(None , 36)
frameCount = 1
elapsedTime = time.time()
fps = 1

fps_text = font.render(f"Pygame FPS: {fps:.2f}", True, RED)
startTIme = time.time()


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pygame FPS")

x=list(range(100))
y=np.sin(x)
# noise_amplitude = 0.2 * np.max(np.abs(y))

def drawGrid():
    for i in range(0, WIDTH, 50):
        pygame.draw.line(screen, GRAY, (i, 0), (i, HEIGHT), 1)

    for j in range(0, HEIGHT, 50):
        pygame.draw.line(screen, GRAY, (j, 0), (j, HEIGHT), 1)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # noise = noise_amplitude * np.random.uniform(-1, 1, len(x))
    # y = np.sin(x + 0.1 * frameCount) + noise
    screen.fill(GRAY)
    drawGrid()
    points = [(int((x[i] / 17) * WIDTH), int((y[i]*0.7 + 1) * HEIGHT / 2)) for i in range(len(x))]
    pygame.draw.lines(screen, BLACK, False, points, 2)
    screen.blit(fps_text, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)
