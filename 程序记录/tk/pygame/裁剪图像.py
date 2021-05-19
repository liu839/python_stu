import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("流光")

turtle = pygame.image.load(r'C:\Users\71037\Desktop\计算机\python\程序记录\pygame\pic\turtle.png')

#0-->未选择 1-->选择中 2-->已选择
select = 0 
select_rect = pygame.Rect(0, 0, 0, 0)
#0-->拖动中 1-->选择中 2-->完成拖动
drag = 0

position = turtle.get_rect()
position.center=width // 2, height // 2

while True:
    for event in pygame.event.get():
    #判断退出
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                #第一次单击,选择范围
                if select == 0 and drag == 0:
                    pos_start = event.pos
                    select = 1
                #第二次单击,拖动图像
                elif select == 2 and drag == 0:
                    capture = screen.subsurface(select_rect).copy()
                    cap_rect = capture.get_rect()
                    drag = 1
                #第三次单击,初始化
                elif select == 2 and drag == 2:
                    select = 0
                    drag = 0
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                #第一次释放,结束选择
                if select == 1 and drag == 0:
                    pos_stop = event.pos
                    select = 2
                #第二次释放,结束拖动
                if select == 2 and drag == 1:
                    drag = 2
    screen.fill(bg)
    screen.blit(turtle, position)

    #绘制选择框
    if select:
        mouse_pos = pygame.mouse.get_pos()
        if select == 1:
            pos_stop = mouse_pos
        
        select_rect.left, select_rect.top = pos_start
        select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
        pygame.draw.rect(screen, (0, 0, 0), select_rect, 1)

    if drag:
        if drag == 1:
            cap_rect.center = mouse_pos
        screen.blit(capture, cap_rect)
    pygame.display.flip()
clock.tick(60)