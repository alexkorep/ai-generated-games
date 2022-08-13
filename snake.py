# Pygame Snake game
# Import the modules needed for the game
import pygame

# Snake tail coordinates
tail = []

# Snake head coordinates, center of the screen
head = [screen_width / 2, screen_height / 2]

# Snake direction
direction = [0, 0]

# Initialize PyGame
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Snake")

# Game loop
running = True
while running:
    # Set the background color
    screen.fill((0, 0, 0))

    # Draw the snake
    for i in range(len(tail)):
        pygame.draw.rect(screen, (255, 255, 255), (tail[i][0] * 50, tail[i][1] * 50, 50, 50))
    pygame.draw.rect(screen, (255, 255, 255), (head[0] * 50, head[1] * 50, 50, 50))

    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = [0, -1]
            elif event.key == pygame.K_DOWN:
                direction = [0, 1]
            elif event.key == pygame.K_LEFT:
                direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                direction = [1, 0]
