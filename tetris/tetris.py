# A Tetris pygame game
# Imports
import pygame
import random

# Possible Tetrominos, array of arrays. Each inner array is a Tetromino. Each Tetromino contains 4 elements, each element
# is a dict with x and y coordinates
# 1: [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 2, 'y': 0}, {'x': 3, 'y': 0}] # I
# 2: [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}] # S
# 3: [{'x': 1, 'y': 0}, {'x': 2, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}] # Z
# 4: [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 2, 'y': 0}, {'x': 2, 'y': 1}] # J
# 5: [{'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 0}] # L
# 6: [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 2, 'y': 0}, {'x': 1, 'y': 1}] # T
# 7: [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}] # O
tetraminos = [
    [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 2, 'y': 0}, {'x': 3, 'y': 0}], # I
    [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}], # S
    [{'x': 1, 'y': 0}, {'x': 2, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}], # Z
    [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 2, 'y': 0}, {'x': 2, 'y': 1}], # J
    [{'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 0}], # L
    [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 2, 'y': 0}, {'x': 1, 'y': 1}], # T
    [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}], # O
]

# Initialize pygame
pygame.init()

# Set the width and height of the screen [480, 640]
screen = pygame.display.set_mode([480, 640])

# Set the title of the window
pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button.
done = False

# Current Tetromino index
current_tetromino_index = 0

# Current tetramino
current_tetromino = tetraminos[current_tetromino_index]

# Tetramino block size
block_size = 20

# Current Tetromino screen coordinates
current_x = 0
current_y = 0

# Current Tetramino falling speed, pixels per frame, 2 initially
speed = 2

# Function to draw the given Tetromino with the given screen coordinates
# parameters:
#   tetromino: the Tetromino to draw
#   x: the x coordinate of the Tetromino
#   y: the y coordinate of the Tetromino
def draw_tetromino(tetromino, x, y):
    # Loop through the Tetromino
    for block in tetromino:
        # Draw the block
        pygame.draw.rect(screen, (255, 0, 0), 
                        (x + block['x'] * block_size, 
                        y + block['y'] * block_size, 
                        block_size, 
                        block_size))


# Function accepts a tetramino and rotates it clockwise
def rotate_tetromino(tetromino):
    # Create a new Tetromino
    new_tetromino = []
    # Loop through the Tetromino
    for block in tetromino:
        # Add the block to the new Tetromino
        new_tetromino.append({'x': -block['y'], 'y': block['x']})
    # Return the new Tetromino
    return new_tetromino


# Main loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # If up key is pressed, rotate the Tetromino clockwise
        # If down key is pressed, move the Tetromino down
        # If left key is pressed, move the Tetromino left
        # If right key is pressed, move the Tetromino right
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_tetromino = rotate_tetromino(current_tetromino)
            elif event.key == pygame.K_DOWN:
                current_y += speed
            elif event.key == pygame.K_LEFT:
                current_x -= speed
            elif event.key == pygame.K_RIGHT:
                current_x += speed

    # --- Game logic should go here
    # Calculate tetramino board coordinates based on current_x and current_y
    tetramino_board_x = current_x // block_size
    tetramino_board_y = current_y // block_size
    
    # Move the Tetromino down with the current speed
    current_y += speed

    # If tetramino board y coordinate reaches the bottom, make a new tetramino
    if tetramino_board_y == 20:
        current_x = 0
        current_y = 0
        current_tetromino_index = random.randint(0, len(tetraminos) - 1)
        current_tetromino = tetraminos[current_tetromino_index]


    # --- Drawing code should go here
    # Set background color to black
    screen.fill((0, 0, 0))

    # Draw the current tetromino
    draw_tetromino(current_tetromino, current_x, current_y)
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Wait 1/60th of a second
    pygame.time.wait(1000 // 60)


