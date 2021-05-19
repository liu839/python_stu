import pygame
import sys
pygame.init()

size = width , height = 600 , 400
speed = [-2,1]
bg = (255, 255, 255)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面")

turtle = pygame.image.load(r"C:\Users\71037\Desktop\计算机\python\程序记录\pygame\pic\turtle.png")

position = turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    position = position.move(speed)
    #移动图像

    if position.left <0 or position.right>width:
        turtle = pygame.transform.flip(turtle , True , False)
        speed[0] = -speed[0]
    
    if position.top < 0 or position.bottom > height:
        #turtle = pygame.transform.flip(turtle , False , True)
        speed[1] = -speed[1]
    
    screen.fill(bg)
    #填充背景,将背景刷白 bg=(255, 255, 255)为RGB色域纯白,刷白之后,之前的乌龟就消失了.

    screen.blit(turtle,position)
    #填充图像,此时重新填充乌龟进去

    pygame.display.flip()
    #刷新页面,Pygame采用双缓冲机制,内部布置好界面后由pygame.display.flip()直接刷新上来

    pygame.time.delay(10)
    #延时10ms执行

    clock.tick(1)
    #锁200帧