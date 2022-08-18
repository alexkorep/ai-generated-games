# Pygame top-down retro-style racing game

# Import modules
import pygame
import random


# Initialize pygame
pygame.init()

# Create screen 600x800 pixels
screen = pygame.display.set_mode((600, 800))

# Set title of screen
pygame.display.set_caption("Racing Game")

# Create player car sprite player_car variable, load from player.png
player_car = pygame.image.load("player.png")
# Scale the player car sprite to 100x100 pixels
player_car = pygame.transform.scale(player_car, (100, 100))

# Create enemy cars sprites, array of 6 images, from car0.png to car5.png
enemy_cars = []
for i in range(6):
    # Load enemy_car variable
    enemy_car = pygame.image.load("car" + str(i) + ".png")
    # Scale the enemy cars sprites to 100x100 pixels
    enemy_car = pygame.transform.scale(enemy_car, (100, 100))
    # Add enemy_car to enemy_cars array
    enemy_cars.append(enemy_car)
    

# Player car postion x
player_car_x = 300

# Enemy cars speed, set to 10
enemy_cars_speed = 2

# Array of enemy car positions, each element is a map with x and y values and car sprite index from enemy_cars array
enemy_cars_pos = []

# Current score
score = 0

# Function to load high score from high_score.txt file
def load_high_score():
    # Return 0, if file does not exist
    try:
        # Open high_score.txt file
        with open("high_score.txt", "r") as f:
            # Read high score from file
            high_score = int(f.read())
            # Return high score
            return high_score
    # If file does not exist, return 0
    except FileNotFoundError:
        return 0

# Function to save high score to high_score.txt file
def save_high_score(score):
    # Open high_score.txt file in write mode
    with open("high_score.txt", "w") as f:
        # Write high score to file
        f.write(str(score))

# Load high score
high_score = load_high_score()

# Function to add a random car on the random position at the top of the screen
def add_enemy_car():
    # Random position x
    enemy_car_x = random.randint(0, 600)
    # Random position y
    enemy_car_y = -100
    # Random car sprite index from enemy_cars array
    enemy_car_sprite = random.randint(0, 5)
    # Add enemy car position to enemy_cars_pos array
    enemy_cars_pos.append({"x": enemy_car_x, "y": enemy_car_y, "sprite": enemy_car_sprite})

# Add enemy car on the screen
add_enemy_car()

# New game function
def new_game():
    # Global variables enemy_cars_pos and player_car_x, and enemy_cars_speed
    global enemy_cars_pos, player_car_x, enemy_cars_speed

    # Reset enemy cars positions
    enemy_cars_pos = []
    # Reset player car position
    player_car_x = 300
    # Add enemy car on the screen
    add_enemy_car()

    # Reset enemy_cars_speed
    enemy_cars_speed = 2

# Game over function
def game_over():
    # Global variables: score and high score
    global score, high_score

    # Draw game over text at the center of the screen
    game_over_text = pygame.font.Font("freesansbold.ttf", 64)
    game_over_surf = game_over_text.render("Game Over", True, (255, 255, 255))
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (300, 100)
    screen.blit(game_over_surf, game_over_rect)

    # Draw "Press space to play again" text at the center of the screen
    play_again_text = pygame.font.Font("freesansbold.ttf", 32)
    play_again_surf = play_again_text.render("Press space to play again", True, (255, 255, 255))
    play_again_rect = play_again_surf.get_rect()
    play_again_rect.midtop = (300, 200)
    screen.blit(play_again_surf, play_again_rect)

    # Print currnt score
    score_text = pygame.font.Font("freesansbold.ttf", 32)
    score_surf = score_text.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_surf.get_rect()
    score_rect.midtop = (300, 300)
    screen.blit(score_surf, score_rect)

    # Print high score
    high_score_text = pygame.font.Font("freesansbold.ttf", 32)
    high_score_surf = high_score_text.render("High Score: " + str(high_score), True, (255, 255, 255))
    high_score_rect = high_score_surf.get_rect()
    high_score_rect.midtop = (300, 350)
    screen.blit(high_score_surf, high_score_rect)
    
    # Update the screen
    pygame.display.flip()

    # Reset score
    score = 0

    # Wait until space is pressed
    while True:
        # Get keyboard events
        for event in pygame.event.get():
            # If space is pressed, start new game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_game()
                    return
            # If event is quit, quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Wait 0.1 seconds
        pygame.time.wait(100)

# Main loop
running = True
while running:
    # Clear background (fill with black)
    screen.fill((0, 0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # If lef key is down, move player car left, if it's not out of the screen
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if player_car_x > 0:
            player_car_x -= 5
    
    # If right key is down, move player car right, if it's not out of the screen
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if player_car_x < 500:
            player_car_x += 5

    # If player hits one of the enemy cars, call game_over function
    for enemy_car in enemy_cars_pos:
        # If player x position is between enemy car position x - 50 and enemy car position x + 50
        # and enemy car position is higher than 600, call game_over function
        if player_car_x > enemy_car["x"] - 50 and player_car_x < enemy_car["x"] + 50 and enemy_car["y"] > 600:
            game_over()

    # Draw player car
    screen.blit(player_car, (player_car_x, 700))

    # Draw enemy cars
    for enemy_car_pos in enemy_cars_pos:
        screen.blit(enemy_cars[enemy_car_pos["sprite"]], (enemy_car_pos["x"], enemy_car_pos["y"]))

    # Increase y position of enemy cars
    for enemy_car_pos in enemy_cars_pos:
        enemy_car_pos["y"] += enemy_cars_speed

    # If enemy car is at the bottom of the screen, remove it from the array
    for enemy_car_pos in enemy_cars_pos:
        if enemy_car_pos["y"] > 800:
            enemy_cars_pos.remove(enemy_car_pos)
            # Incremeent score
            score += 1
            # If score is higher than high score, set high score to score
            if score > high_score:
                high_score = score
                # Save high score to file
                save_high_score(high_score)

    # If the last enemy car is below 100 pixels, add a new enemy car
    if enemy_cars_pos[len(enemy_cars_pos) - 1]["y"] > 100:
        add_enemy_car()

    # Increase enemy car speed by 0.1%
    enemy_cars_speed += enemy_cars_speed * 0.001

    # Draw score text
    score_text = pygame.font.Font("freesansbold.ttf", 32)
    score_surf = score_text.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_surf.get_rect()
    score_rect.midtop = (300, 50)
    screen.blit(score_surf, score_rect)

    # Draw high score text
    high_score_text = pygame.font.Font("freesansbold.ttf", 32)
    high_score_surf = high_score_text.render("High score: " + str(high_score), True, (255, 255, 255))
    high_score_rect = high_score_surf.get_rect()
    high_score_rect.midtop = (300, 100)
    screen.blit(high_score_surf, high_score_rect)

    # Update screen
    pygame.display.update()
    # Wait 1/60 seconds
    pygame.time.delay(10)
