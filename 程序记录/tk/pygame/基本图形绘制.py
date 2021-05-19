import pygame
import sys
from pygame.locals import *
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = width , height = 640 , 200   #界面尺寸
screen = pygame.display.set_mode(size)
pygame.display.set_caption("流光")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        #判断退出
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (50, 50, 150, 50), 0)
    pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
    pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10)

    pygame.display.flip()

    clock.tick(10)