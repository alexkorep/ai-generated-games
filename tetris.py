# Pygame Tetris game
#
# This is a simple Tetris game written in Python using Pygame.

# Import the modules needed for the game
import pygame
import random
import os
import sys
import time
import math


# Initialize PyGame
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Tetris")

# Initialize array of possible tetraminos
# Possible tetraminos are: 
# ##
#  ##

