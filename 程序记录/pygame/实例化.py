import pygame
import sys
from pygame.locals import *
pygame.init()

size = width , height = 600 , 400
speed = [0, 0]
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面")

turtle = pygame.image.load(r"C:\Users\71037\Desktop\计算机\python\程序记录\pygame\pic\turtle.png")
position = turtle.get_rect()

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    speed=[0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F11:
                FULLSCREEN = not FULLSCREEN
                if FULLSCREEN:
                    screen = pygame.display.set_mode((1920,1080),
                    FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)
            if event.key == K_LEFT or event.key == K_a:
                speed[0] -= 1
                turtle = l_head
            if event.key == K_RIGHT or event.key == K_d:
                speed[0] += 1
                turtle = r_head
            if event.key == K_UP or event.key == K_w:
                speed[1] -= 1
            if event.key == K_DOWN or event.key == K_s:
                speed[1] += 1
        

    if position.left <0:
        speed[0]=1
    elif position.right>width:
        speed[0]=-1
    elif position.top < 0:
        speed[1]=1
    elif position.bottom > height:
        speed[1]=-1

    position = position.move(speed)
    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.flip()
    pygame.time.delay(10)