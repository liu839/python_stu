import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, heigth = 640, 480
bg = (0 ,0 ,0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("流光")

turtle = pygame.image.load(r"C:\Users\71037\Desktop\计算机\python\程序记录\pygame\pic\turtle.png").convert_alpha()
background = pygame.image.load(r"C:\Users\71037\Desktop\计算机\python\程序记录\pygame\pic\background.jpg").convert()
position = turtle.get_rect()
position.center= width // 2, heigth // 2

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    screen.blit(background,(0,0))
    blit_alpha(screen, turtle, position, 200)

    pygame.display.flip()
    clock.tick(30)