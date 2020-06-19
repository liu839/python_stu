import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 640, 480
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(szie)
pygame.display.set_caption(流光)

turtle = pygame.image.load('/pic/turrle.png')
position = turtle.rect = turtle.get_rect()

speed = [5, 0]
turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle

turtle = turtle_top

while True:
    for evnent in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        position=position.move(speed)

    s
