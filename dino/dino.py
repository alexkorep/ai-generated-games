# Clone of the classic game Dino from Chrome, using Pygame
# Load modules
import pygame
import random

# Initialize pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Dino")

# Player
playerImg = pygame.image.load('dino.png')
# Scale player to 50x50
playerImg = pygame.transform.scale(playerImg, (50, 50))

# Set player position to bottom left, 50 pixels from the left edge, 100 pixels from the bottom
playerX = 50
playerY = 500

# Array of cactus images
cactusImg = []

# Load 2 cactus images
cactusImg.append(pygame.image.load('cactus1.png'))
cactusImg.append(pygame.image.load('cactus2.png'))

# Scale all cactus images to 50x50
for i in range(len(cactusImg)):
    cactusImg[i] = pygame.transform.scale(cactusImg[i], (50, 50))

# Array of cactus positions
cactusX = []

# Array of cacuts image ids in cacutsImg array
cactusImgId = []

# current speed
speed = 5

# Player vertical speed
playerYspeed = 0

# Current score
score = 0

# Hight score
high_score = 0

# Load high score from file
try:
    with open('high_score.txt', 'r') as f:
        high_score = int(f.read())
except:
    pass

# Function to save high score to file
def save_high_score():
    with open('high_score.txt', 'w') as f:
        f.write(str(high_score))

# Function to reset the game
def reset():
    # Reset player position
    global playerX, playerY, playerYspeed, speed
    playerX = 50
    playerY = 500
    playerYspeed = 0

    # Reset cactus array
    cactusX.clear()
    cactusImgId.clear()

    # Reset speed
    speed = 5

    # Reset score
    global score
    score = 0

# Game over function (game_over)
def game_over():
    # Draw game over message with black font color
    game_over_font = pygame.font.Font('freesansbold.ttf', 64)
    game_over_text = game_over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game_over_text, (200, 250))

    # Update the screen
    pygame.display.update()

    # Wait for 1 second
    pygame.time.delay(1000)

    # Reset the game
    reset()


# Function to add a cactus to the array
def addCactus():
    # If cactus array is empty, or last cactus is more than 200 pixels away from the right edge,
    # add a new cactus to the array with probablilty 1/10
    if len(cactusX) == 0 or cactusX[-1] < 600:
        if random.randint(1, 10) == 1:
            cactusX.append(800)
            cactusImgId.append(random.randint(0, 1))


# Main game loop
running = True
while running:
    ###### Calculation ######

    # Shift all cacuts to the left
    for i in range(len(cactusX)):
        cactusX[i] -= speed
    
    # If first cactus is out of screen to the left, remove it
    if len(cactusX) > 0 and cactusX[0] < -100:
        cactusX.pop(0)
        cactusImgId.pop(0)
        # Increase score
        score += 1
        # Increase speed
        speed += 0.1
        # If score is higher than high score, update high score
        if score > high_score:
            high_score = score
            save_high_score()
    
    # Add a new cactus
    addCactus()

    # Add vertical speed to player position
    playerY += playerYspeed

    # If player below the ground, set player position to ground and set vertical speed to 0
    if playerY >= 500:
        playerY = 500
        playerYspeed = 0
    # If player is not on the ground, add gravity to vertical speed
    else:
        playerYspeed += 1

    # Game over flag
    game_over_flag = False

    # Check if player collides with any cactus
    for i in range(len(cactusX)):
        if abs(playerX - cactusX[i]) < 50 and abs(playerY - 500) < 50:
            # Set game over flag
            game_over_flag = True
    
    # If game over flag is set, call game_over function
    if game_over_flag:
        game_over()

    ###### Draw ######

    # Fill with white background
    screen.fill((255, 255, 255))
    
    screen.blit(playerImg, (playerX, playerY))

    # Draw the ground, black line 100 pixels from the bottom
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (800, 600), 100)

    # Draw the cacti
    for i in range(len(cactusX)):
        screen.blit(cactusImg[cactusImgId[i]], (cactusX[i], 500))

    # Draw score
    score_font = pygame.font.Font('freesansbold.ttf', 32)
    score_text = score_font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Draw high score
    high_score_font = pygame.font.Font('freesansbold.ttf', 32)
    high_score_text = high_score_font.render("High Score: " + str(high_score), True, (0, 0, 0))
    screen.blit(high_score_text, (10, 50))


    ###### Events ######
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If dino is not jumping, and space is pressed, make dino jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space",playerYspeed)
                if playerYspeed == 0:
                    playerYspeed = -15
            
    ###### Update ######
    pygame.display.update()

    # Wait 1 msec
    pygame.time.wait(16)