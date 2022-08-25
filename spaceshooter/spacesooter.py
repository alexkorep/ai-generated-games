# Space shooter game with pygame
# Include pygame
import pygame
import random

# Iniiialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((480, 640))

# Title and icon
pygame.display.set_caption("Space Shooter")

# Background
background = pygame.image.load("img/back3.jpeg")
# Resize the background
background = pygame.transform.scale(background, (480, 640))

# Load the player
player = pygame.image.load("img/ships/ship-player.png")
# Resize the player to 100x100
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
player = pygame.transform.scale(player, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Player position
player_x = 200
player_y = 500

# Player speed
player_speed = 5

# Array of bullet coordinates, (x, y)
bullets = []

BULLET_SPEED = 20

ENEMY_DENSITY = 100

# Array of enemy images
enemy_images = []
# Load 8 enemy images, each ship has name "img/ships/ship01.png", "img/ships/ship02.png", ...
for i in range(8):
    enemy_images.append(pygame.image.load("img/ships/ship0" + str(i + 1) + ".png"))
    # Resize the enemy images to 100x100
    enemy_images[i] = pygame.transform.scale(enemy_images[i], (PLAYER_WIDTH, PLAYER_HEIGHT))

# Array of enemy positions and horizontal shift, (x, y, shift, image_index)
enemies = []

# Function to add an enemy at a random position on the top of the screen and zero shift
def generate_enemy():
    enemy_x = random.randint(0, 480 - PLAYER_WIDTH)
    enemy_y = -PLAYER_HEIGHT
    enemy_shift = random.randint(-1, 1)
    enemy_image_index = random.randint(0, len(enemy_images) - 1)
    enemies.append([enemy_x, enemy_y, enemy_shift, enemy_image_index])

# Enemy speed
enemy_speed = 2

# New game function
def new_game():
    # Globals
    global player_x, player_y
    global enemies
    global bullets

    # Reset player x and y position
    player_x = 200
    player_y = 500


    # Reset enemies
    enemies.clear()

    # Reset bullets
    bullets.clear()

    # Reset score
    global score
    score = 0

    # Reset enemy speed
    global enemy_speed
    enemy_speed = 2


# Game over function
def game_over():
    # Draw game over text
    game_over_text = pygame.font.Font("freesansbold.ttf", 64)
    game_over_surf = game_over_text.render("Game over", True, (255, 255, 255))
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (240, 10)
    screen.blit(game_over_surf, game_over_rect)

    # Draw "Press enter to continue" text
    press_enter_text = pygame.font.Font("freesansbold.ttf", 32)
    press_enter_surf = press_enter_text.render("Press enter to continue", True, (255, 255, 255))
    press_enter_rect = press_enter_surf.get_rect()
    press_enter_rect.midtop = (240, game_over_rect.height + 10)

    # Wait for the player to press Enter key
    pygame.display.flip()
    waiting = True
    while waiting:
        # If the player presses Enter key, then waiting is False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

    # Call new game function
    new_game()

# Current score
score = 0

# Load high score from file, if it exists
try:
    with open("high_score.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 0

# Function to save high score to file
def save_high_score():
    with open("high_score.txt", "w") as f:
        f.write(str(high_score))


# Main loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Check if cursor keys are down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Check if spacebar is down, if so, add a bullet to the array
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + PLAYER_WIDTH // 2, player_y])

    # If player is out of the screen, set it to the opposite side
    if player_x < 0:
        player_x = 0
    if player_x > screen.get_width() - PLAYER_WIDTH:
        player_x = screen.get_width() - PLAYER_WIDTH
    if player_y < 0:
        player_y = 0
    if player_y > screen.get_height() - PLAYER_HEIGHT:
        player_y = screen.get_height() - PLAYER_HEIGHT

    # Add an enemy with random probablity of 1 in ENEMY_DENSITY, or if there are not enemies
    if len(enemies) == 0 or random.randint(0, ENEMY_DENSITY) == 1:
        generate_enemy()
    

    # Move the enemies down
    for i in range(len(enemies)):
        enemies[i][1] += enemy_speed
        # If the enemy is out of the screen, remove it from the array
        if enemies[i][1] > screen.get_height():
            enemies[i] = None
    # Filter out enemies which are None
    enemies = list(filter(None, enemies))
    
    


    # Update bullets
    for i in range(len(bullets)):
        bullets[i][1] -= BULLET_SPEED
        if bullets[i][1] < 0:
            bullets[i] = None
    # Delete bullets which are None from the array
    bullets = list(filter(None, bullets))

    # Check if the player is hit by an enemy
    for i in range(len(enemies)):
        if player_x <= enemies[i][0] + PLAYER_WIDTH and player_x + PLAYER_WIDTH >= enemies[i][0] and player_y <= enemies[i][1] + PLAYER_HEIGHT and player_y + PLAYER_HEIGHT >= enemies[i][1]:
            game_over()
            break

    # Array of bullets to delete
    bullets_to_delete = []
    # Check if any enemy is hit by a bullet
    for i in range(len(enemies)):
        for j in range(len(bullets)):
            if enemies[i][0] <= bullets[j][0] <= enemies[i][0] + PLAYER_WIDTH and enemies[i][1] <= bullets[j][1] <= enemies[i][1] + PLAYER_HEIGHT:
                enemies[i] = None
                # Increment score
                score += 1
                # If score is greater than high score, set high score to score
                if score > high_score:
                    high_score = score
                    # Save high score to file
                    save_high_score()

                # Increment enemy_speed by 5%
                enemy_speed += 0.05

                # Add j to the array of bullets to delete
                bullets_to_delete.append(j)
                break
    # Delete enemies which are None from the array
    enemies = list(filter(None, enemies))
    # Set bullets to None from the array of bullets to delete
    for i in range(len(bullets_to_delete)):
        bullets[bullets_to_delete[i]] = None
    # Delete bullets which are None from the array
    bullets = list(filter(None, bullets))
    

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the player
    screen.blit(player, (player_x, player_y))

    # Draw the enemies
    for i in range(len(enemies)):
        image_index = enemies[i][3]
        x = enemies[i][0]
        y = enemies[i][1]
        screen.blit(enemy_images[image_index], (x,y))

    # Draw the bullets, each bullet is a white circle with a radius of 5
    for bullet in bullets:
        pygame.draw.circle(screen, (255, 255, 255), bullet, 5)

    # Draw the score
    score_text = pygame.font.Font("freesansbold.ttf", 32)
    score_surf = score_text.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_surf.get_rect()
    score_rect.midtop = (screen.get_width() // 2, 10)
    screen.blit(score_surf, score_rect)
    # Draw the high score
    high_score_text = pygame.font.Font("freesansbold.ttf", 32)
    high_score_surf = high_score_text.render("High Score: " + str(high_score), True, (255, 255, 255))
    high_score_rect = high_score_surf.get_rect()
    high_score_rect.midtop = (screen.get_width() // 2, 50)
    screen.blit(high_score_surf, high_score_rect)

    # Make 16 msec delay
    pygame.time.delay(16)

    # Update screen
    pygame.display.flip()
