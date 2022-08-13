# Space Invaders game with pygame
import pygame
import random

# Initialize PyGame
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Space Invaders")

# Initialize the array of invaders
invaders = []

# Initialize the array of invaders' velocities
invader_velocities = []

# Initialize player's position
player_x = screen_width / 2
player_y = screen_height - 50

# Initialize player's array of bullets
player_bullets = []

# Fill the screen with invaders
for i in range(10):
    # Initialize the invader
    invader = []
    # Initialize the invader's velocity
    invader_velocity = []
    # Initialize the invader's position
    invader_x = random.randint(0, screen_width - 50)
    invader_y = random.randint(0, screen_height - 50)
    # Initialize the invader's velocity
    invader_velocity_x = random.randint(-5, 5)
    invader_velocity_y = random.randint(-5, 5)
    # Add the invader to the array
    invaders.append([invader_x, invader_y])
    # Add the invader's velocity to the array
    invader_velocities.append([invader_velocity_x, invader_velocity_y])

# Game loop
running = True
while running:
    # Set the background color
    screen.fill((0, 0, 0))
    # Draw the player
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, 50, 50))
    # Draw the invaders
    for i in range(len(invaders)):
        pygame.draw.rect(screen, (255, 255, 255), (invaders[i], invader_velocities[i]))

    # Update invader's position
    for i in range(len(invaders)):
        invaders[i][0] += invader_velocities[i][0]
        invaders[i][1] += invader_velocities[i][1]
        # Check if the invader has passed the screen
        if invaders[i][0] < 0:
            invaders[i][0] = 0
            invader_velocities[i][0] = -invader_velocities[i][0]
        if invaders[i][0] > screen_width - 50:
            invaders[i][0] = screen_width - 50
            invader_velocities[i][0] = -invader_velocities[i][0]
        if invaders[i][1] < 0:
            invaders[i][1] = 0
            invader_velocities[i][1] = -invader_velocities[i][1]
        if invaders[i][1] > screen_height - 50:
            invaders[i][1] = screen_height - 50
            invader_velocities[i][1] = -invader_velocities[i][1]

    # Draw the player's bullets
    for i in range(len(player_bullets)):
        pygame.draw.rect(screen, (255, 255, 255), (player_bullets[i][0], player_bullets[i][1], 5, 5))

    # Update bullet positions
    for i in range(len(player_bullets)):
        player_bullets[i][1] -= 10
        if player_bullets[i][1] < 0:
            # Set bullet to None to remove it from the array
            player_bullets[i] = None

    # Delete bullets which are None
    player_bullets = [bullet for bullet in player_bullets if bullet is not None]

    # Update the screen
    pygame.display.flip()
    # Check if the player has collided with an invader
    # for i in range(len(invaders)):
    #     if invaders[i] < player_x < invaders[i] + 50 and invader_velocities[i] < player_y < invader_velocities[i] + 50:
    #         running = False
        
    # Control the player with left and right arrows
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 50
            if event.key == pygame.K_RIGHT:
                player_x += 50

        # Exit the game if ESC is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # If space is pressed, shoot a bullet
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        player_bullets.append([player_x, player_y])
