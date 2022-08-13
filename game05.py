import pygame
import sys
import random

pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

asteroid = pygame.image.load("asteroid.png")
asteroidrect = asteroid.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    asteroidrect = asteroidrect.move(speed)
    if asteroidrect.left < 0 or asteroidrect.right > width:
        speed[0] = -speed[0]
    if asteroidrect.top < 0 or asteroidrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(asteroid, asteroidrect)
    pygame.display.flip()