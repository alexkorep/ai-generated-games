# Flappy Bird clone in Python 3 using PyGame

import asyncio
import pygame
import random
from os import path

# Initialize PyGame
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Flappy Bird")


# Initialize the bird
bird_x = 50
bird_y = 50

# Initialize the bird's velocity
bird_velocity = 0

# Initialize the bird's acceleration
bird_acceleration = 0.5

# Initialize the bird's score
bird_score = 0

# Load bird from bird.png
bird_image = pygame.image.load("bird.png")

# Load background from background.jpg
background_image = pygame.image.load("background.jpg")

# Load pipe from pipe.png
pipe_image = pygame.image.load("pipe.png")

# Load explosion image from explosion.png
explosion_image = pygame.image.load("explosion.png")

# Load high score from disk
def load_high_score():
    # Check if the file exists
    if not path.exists("high_score.txt"):
        # If it doesn't, create it
        save_high_score(0)
        # Return 0
        return 0

    # Open the file
    with open("high_score.txt", "r") as file:
        # Read the file
        high_score = int(file.read())
    # Return the high score
    return high_score

# Save high score to disk
def save_high_score(high_score):
    # Open the file
    with open("high_score.txt", "w") as file:
        # Write the file
        file.write(str(high_score))

# Init high score
high_score = load_high_score()

# Create array of pipes
pipes = []

# Set the gap between the pipes to 300
pipe_gap = 200

# Set pipe movement speed to -5 pixels per frame
pipe_movement_speed = -5

# Show explosion flag
show_explosion = False

# Create a pipe
def create_pipe():
    global pipe_gap

    # Create a pipe
    pipe = [screen_width, random.randint(100, screen_height - 200), pipe_gap]
    # Add the pipe to the array of pipes
    pipes.append(pipe)

    # Make pipe_gap smaller by 5%
    pipe_gap -= pipe_gap * 0.05

# Create a first pipe
create_pipe()

# New game function
def new_game():
    # define globals
    global bird_x, bird_y, bird_velocity, bird_acceleration, bird_score, pipes, pipe_gap

    # Reset the bird's position
    bird_x = 50
    bird_y = 50
    # Reset the bird's velocity
    bird_velocity = 0
    # Reset the bird's acceleration
    bird_acceleration = 0.5
    # Reset the bird's score
    bird_score = 0
    # Reset pipe_gap
    pipe_gap = 200

    # Reset the pipes
    pipes = []
    # Create a first pipe
    create_pipe()

async def main():
    # Import globals
    global bird_x, bird_y, bird_velocity, bird_acceleration, bird_score, pipes, pipe_gap, show_explosion, high_score

    # Game loop
    running = True
    while running:
        # Draw the background, scale it to the screen size and blit it to the screen
        screen.blit(pygame.transform.scale(background_image, (screen_width, screen_height)), (0, 0))

        # Check for events
        for event in pygame.event.get():
            # Check if the user clicked the red button
            if event.type == pygame.QUIT:
                running = False
            # Check if the user pressed the space bar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -10
                    bird_acceleration = 0.5

        # Update the bird's position
        bird_velocity += bird_acceleration
        bird_y += bird_velocity

        # Create a new pipe if the bird position is between the fist pipe and first pipe + pipe_movement_speed
        if pipes[0][0] + pipe_movement_speed <= bird_x < pipes[0][0]:
            bird_score += 1
            if bird_score > high_score:
                high_score = bird_score
                save_high_score(high_score)


        # If the distance between the last pipe and the right of the screen is more than 300, create a new pipe
        if pipes[-1][0] < screen_width - 300:
            create_pipe()

        # If the first pipe is past the left of the screen, remove it
        if pipes[0][0] < -100:
            pipes.pop(0)

        # Update the pipes' position
        for pipe in pipes:
            pipe[0] += pipe_movement_speed

        # Check if the bird has collided with the pipe
        for pipe in pipes:
            if bird_x + 50 > pipe[0] and bird_x + 50 < pipe[0] + 50:
                if bird_y + 50 < pipe[1] or bird_y + 50 > pipe[1] + pipe[2]:
                    show_explosion = True

        # Check if the bird has collided with the ground
        if bird_y + 50 > screen_height:
            # Game over
            new_game()

        # Check if the bird has passed the pipe
        if bird_x > screen_width:
            bird_x = 0
            bird_y = 50
            bird_velocity = 0
            bird_acceleration = 0.5
            bird_score = 0
            pipes = []

        # Draw the pipes
        for pipe in pipes:
            screen.blit(pygame.transform.scale(pipe_image, (50, pipe[1])), (pipe[0], 0))
            screen.blit(pygame.transform.scale(pipe_image, (50, screen_height - pipe[1] - pipe[2])), (pipe[0], pipe[1] + pipe[2]))

        # Draw the bird, scale it to 100x100 and blit it to the screen
        screen.blit(pygame.transform.scale(bird_image, (100, 100)), (bird_x, bird_y))

        # Draw the bird's score
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("Score: " + str(bird_score), True, (255, 255, 255))
        screen.blit(text, (10, 10))

        # Draw the high score
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("High Score: " + str(high_score), True, (255, 255, 255))
        screen.blit(text, (10, 50))

        # Draw explosion
        if show_explosion:
            # Draw the explosion image and blit it to the screen
            screen.blit(pygame.transform.scale(explosion_image, (100, 100)), (bird_x, bird_y))

        # Update the screen
        pygame.display.flip()

        # Wair for 15 milliseconds, or for 500 milliseconds if show_explosion
        if show_explosion:
            pygame.time.wait(500)
            # Hide the explosion
            show_explosion = False
            # Game over
            new_game()

        else:
            pygame.time.wait(15)

asyncio.run( main() )
