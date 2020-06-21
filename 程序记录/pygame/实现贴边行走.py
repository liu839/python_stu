import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 640, 480
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("流光")

turtle = pygame.image.load(r'C:\Users\71037\Desktop\计算机\python\程序记录\pygame\pic\turtle.png')
position = turtle_rect = turtle.get_rect()

speed = [5, 0]
turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle

turtle = turtle_top

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    position=position.move(speed)

    if position.right > width:
        turtle = turtle_right
        position = turtle_rect = turtle.get_rect()
        #矩形尺寸的改变导致位置也有变化
        position.left = width - turtle_rect.width
        speed = [0, 5]

    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        #矩形尺寸的改变导致位置也有变化
        position.top = height - turtle_rect.height
        speed = [0, -5]

    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        #矩形尺寸的改变导致位置也有变化

        speed = [5, 0]

    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        #矩形尺寸的改变导致位置也有变化
        position.left = width - turtle_rect.width
        position.top = height - turtle_rect.height
        speed = [-5, 0]


    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.flip()

    clock.tick(60)