# Import pygame module
import pygame
# Import random module
import random

# Initialize pygame
pygame.init()

# Create a vertical screen
# with width of 600 and height of 800
screen = pygame.display.set_mode((600, 800))

# Set the title of the window
pygame.display.set_caption("Red Light Green Light")

# Set the background color to white
screen.fill((255, 255, 255))

# Player coordinates, initial position is the middle bottom of the screen
player_x = 300
player_y = 740

# Current light, either red or green. Initial is red
current_light = "red"

# Game state variable:
# 0 - Game is started
# 1 - Game is over, you win
# 2 - Game is over, you lose

game_state = 0

# Declare current score
current_score = 0

# Game loop, infinite until Escape is pressed
while True:
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw player as a blue square
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, 50, 50))

    # If game state is game is started
    if game_state == 0:
        # Draw the current light as a red or green square
        if current_light == "red":
            pygame.draw.rect(screen, (255, 0, 0), (300, 0, 100, 100))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (300, 0, 100, 100))

        # Draw the current score at top left corner of the screen
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("Score: " + str(current_score), True, (0, 0, 0))
        screen.blit(text, (0, 0))

        # If mouse is down, move player 10 pixels up
        # If the light was red, set game state to you lose
        # Otherwise do nothing
        if pygame.mouse.get_pressed()[0]:
            player_y -= 10
            if current_light == "red":
                game_state = 2
                # Decrement current score by 1
                current_score -= 1

        # If player reached the top of the screen, set game state to you win
        if player_y < 0:
            game_state = 1
            # Increment current score by 1
            current_score += 1

    # If game state is you win, draw you win text
    if game_state == 1:
        text = pygame.font.Font(None, 100).render("You win! Press Enter", True, (0, 0, 0))
        screen.blit(text, (100, 300))

        # If Enter is pressed, set game state to game started and initialize player coordinates
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            game_state = 0
            player_x = 300
            player_y = 740

    # If game state is you lose, draw you lose text
    if game_state == 2:
        text = pygame.font.Font(None, 100).render("You lose! Press Enter", True, (0, 0, 0))
        screen.blit(text, (100, 300))

        # If Enter is pressed, set game state to game started and initialize player coordinates
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            game_state = 0
            player_x = 300
            player_y = 740
    
    # Randomly change the current light
    if random.randint(0, 100) == 0:
        current_light = "green" if current_light == "red" else "red"


    # Update the screen
    pygame.display.update()

    # If Escape is pressed, exit the game
    for event in pygame.event.get():
        # If ESC is pressed, exit the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
