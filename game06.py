# Write Flappy Bird game with PyGame:

import pygame
from random import randint
from pygame.locals import *
from sys import exit
import time

pygame.init()

screen = pygame.display.set_mode((288, 512), 0, 32)

background = pygame.image.load('assets/sprites/background-day.jpeg').convert()
#base = pygame.image.load('assets/sprites/base.png').convert()

pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()
score_font = pygame.font.SysFont("Arial", 16)

def create_pipe():
    rand = randint(20, 100)
    pipe_upper = pygame.image.load('assets/sprites/pipe-green-upper.png').convert()
    pipe_lower = pygame.image.load('assets/sprites/pipe-green-lower.png').convert()
    pipe_upper.set_colorkey((0, 0, 0))
    pipe_lower.set_colorkey((0, 0, 0))
    pipe_upper = pygame.transform.rotate(pipe_upper, 180)
    pipe_upper.set_clip(pygame.Rect(0, 0, pipe_upper.get_width() - 10, pipe_upper.get_height()))
    # pipe_upper.add_internal_offset((- pipe_upper.get_width() + 10, 0))
    pipe_lower.set_clip(pygame.Rect(0, 0, pipe_lower.get_width() - 10, pipe_lower.get_height()))
    # pipe_lower.add_internal_offset((- pipe_lower.get_width() + 10, 0))
    pipe_upper = pygame.transform.scale(pipe_upper, (pipe_upper.get_width() // 2, pipe_upper.get_height() // 2))
    pipe_lower = pygame.transform.scale(pipe_lower, (pipe_lower.get_width() // 2, pipe_lower.get_height() // 2))
    # pipe_upper.set_pos((288, rand - pipe_upper.get_height()))
    # pipe_lower.set_pos((288, rand + 100))
    return pipe_upper, pipe_lower

def is_off_screen(sprite):
    return sprite.get_pos()[0] < -(sprite.get_width())

pipes = [create_pipe()]

def is_collided(bird, upper_pipe, lower_pipe):
    bird_mask = bird.get_mask()
    upper_mask = upper_pipe.get_mask()
    lower_mask = lower_pipe.get_mask()

    pipe_offset = (upper_pipe.get_pos()[0] - bird.get_pos()[0], upper_pipe.get_pos()[1] - round(bird.get_pos()[1]))
    b_point = bird_mask.overlap(upper_mask, pipe_offset)

    pipe_offset = (lower_pipe.get_pos()[0] - bird.get_pos()[0], lower_pipe.get_pos()[1] - round(bird.get_pos()[1]))
    b_point = bird_mask.overlap(lower_mask, pipe_offset)

    if b_point:
        return True
    
    return False

bird = pygame.image.load('assets/sprites/redbird-upflap.png').convert()
bird.set_colorkey((255, 255, 255))
bird = pygame.transform.scale(bird, (bird.get_width() // 2, bird.get_height() // 2))
bird_rect = bird.get_rect()
bird_rect[0] = screen.get_width() // 2
bird_rect[1] = screen.get_height() // 2
bird_mask = pygame.mask.from_surface(bird)
bird_speed = 0
bird_gravity = 0.25

game_active = True
score = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird_speed = -3.5

    screen.blit(background, (0, 0))

    if game_active:
        # update bird
        bird_speed += bird_gravity
        rotated_bird = pygame.transform.rotate(bird, -bird_speed * 5)
        bird_rect[1] += round(bird_speed)
        screen.blit(rotated_bird, bird_rect)

        # update pipes
        for pipe in pipes:
            pipe[0].set_pos((pipe[0].get_pos()[0] - 1, pipe[0].get_pos()[1]))
            pipe[1].set_pos((pipe[1].get_pos()[0] - 1, pipe[1].get_pos()[1]))

            # draw pipes
            screen.blit(pipe[0], pipe[0].get_pos())
            screen.blit(pipe[1], pipe[1].get_pos())

            # check for pipe collision
            if is_collided(bird_rect, pipe[0], pipe[1]):
                game_active = False

            # check for off screen pipes
            if is_off_screen(pipe[0]) or is_off_screen(pipe[1]):
                pipes.remove(pipe)

        # check for new pipes
        if len(pipes) < 2 and not is_off_screen(pipes[-1][0]):
            pipes.append(create_pipe())

        # check for score
        if pipes[0][0].get_pos()[0] < bird_rect.right:
            score += 1
        score_text = score_font.render("Score: " + str(score), 1, (0, 0, 0))
        screen.blit(score_text, (10, 10))

    else:
        # display game over
        pass

    # update screen
    pygame.display.update()
    clock.tick(120)