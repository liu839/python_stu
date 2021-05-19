import pygame
import sys
from pygame.locals import *
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#points = [(200, 75), (300 ,25), (400, 75), (450, 25), (450, 125), (400, 75), (300, 125)]
size = width , height = 640 , 500   #界面尺寸
screen = pygame.display.set_mode(size)
pygame.display.set_caption("流光")

moving =False
position = size[0]//2, size[1]//2 
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        #判断退出
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                moving = False
        
        if moving:
            position = pygame.mouse.get_pos()
    screen.fill(WHITE)

    #多边形绘制
    #pygame.draw.polygon(screen, GREEN, points, 0)
    #线段绘制
    #pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
    #pygame.draw.lines(Surface, color, closed, pointlist, width=1) #closed设置为true或1 线段为首尾相连
    #抗锯齿
    #pygame.draw.aaline(Surface, color, startpos, endpos, blend=1)
    #pygame.draw.aalines(Surface, color, closed, pointlist, blend=1)

    pygame.draw.circle(screen, RED, position, 25, 1)
    pygame.draw.circle(screen, GREEN, position, 75, 1)
    pygame.draw.circle(screen, BLUE, position, 125, 1)
    


    pygame.display.flip()

    clock.tick(144)