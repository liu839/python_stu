import pygame
import sys
from pygame.locals import *
pygame.init()

size = width , height = 600 , 400   #界面尺寸
speed = [0, 0]                      #运动速度
bg = (255, 255, 255)                #背板颜色
ratio = 1.0                         #缩放比例


clock = pygame.time.Clock()
screen = pygame.display.set_mode(size,RESIZABLE)
pygame.display.set_caption("初次见面")

turtle = pygame.image.load(r"C:\Users\71037\Desktop\计算机\python\程序记录\pygame\pic\turtle.png")
oturtle = turtle
oturtle_rect= oturtle.get_rect()

position = turtle_rect = oturtle_rect

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    speed=[0, 0]
    for event in pygame.event.get():
    #判断退出
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
    
    if event.type == VIDEORESIZE:
    #检测窗口化
        size = event.size
        width, height = size
        print(size)
        screen = pygame.display.set_mode(size, RESIZABLE)
    if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
    #放大或者缩小乌龟
        if event.key == K_EQUALS and ratio<2.0:
            ratio += 0.1
        if event.key == K_MINUS and ratio>0.5:
            ratio -= 0.1
        if event.key == K_SPACE:
            ratio = 1.0

    if position.left <0:
    #调换方向
        speed[0]=1
    elif position.right>width:
        speed[0]=-1
    elif position.top < 0:
        speed[1]=1
    elif position.bottom > height:
        speed[1]=-1
    
    #刷新页面
    position = position.move(speed)
    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.flip()

    pygame.time.delay(10)