# Pygame Sokoban game
# Import the modules needed for the game
import pygame

# Game levels: array of blocks, with the following legend:
# 0: empty space
# 1: wall
# 2: box
# 3: player
# 4: goal
# 5: box on goal
# 6: player on goal

levels = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 4, 4, 1],
        [1, 0, 2, 2, 2, 4, 4, 1],
        [1, 0, 2, 3, 2, 0, 0, 1],
        [1, 0, 2, 2, 2, 4, 4, 1],
        [1, 0, 0, 0, 0, 4, 4, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]
]

# Initialize PyGame
pygame.init()

# Set the width and height of the screen [600, 600]
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Sokoban")

# Initialize current level
current_level = 0

# Main game loop
running = True
while running:
    # Set the background color
    screen.fill((0, 0, 0))

    # Draw the level
    for i in range(len(levels[current_level])):
        for j in range(len(levels[current_level][i])):
            if levels[current_level][i][j] == 0:
                pygame.draw.rect(screen, (0, 0, 0), (j * 50, i * 50, 50, 50))
            elif levels[current_level][i][j] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (j * 50, i * 50, 50, 50))
            elif levels[current_level][i][j] == 2:
                pygame.draw.rect(screen, (255, 255, 0), (j * 50, i * 50, 50, 50))
            elif levels[current_level][i][j] == 3:
                pygame.draw.rect(screen, (255, 0, 0), (j * 50, i * 50, 50, 50))
            elif levels[current_level][i][j] == 4:
                pygame.draw.rect(screen, (0, 255, 0), (j * 50, i * 50, 50, 50))
            elif levels[current_level][i][j] == 5:
                pygame.draw.rect(screen, (0, 0, 255), (j * 50, i * 50, 50, 50))
            elif levels[current_level][i][j] == 6:
                pygame.draw.rect(screen, (0, 255, 255), (j * 50, i * 50, 50, 50))

    # Update the screen
    pygame.display.flip()

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Move the player left
                # Loop through the level to check if the player can move left

    