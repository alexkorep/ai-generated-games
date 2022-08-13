import pygame
from pygame.locals import *
import sys

pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (speed[0] -1) * 2
            elif event.key == K_RIGHT:
                speed[0] = speed[0] if speed[0] == 0 else (speed[0] +1) * 2
            elif event.key == K_UP:
                speed[1] = speed[1] if speed[1] == 0 else (speed[1] -1) * 2
            elif event.key == K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (speed[1] +1) * 2
            elif event.key == K_ESCAPE:
                sys.exit()
            else:
                print(event.key)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()