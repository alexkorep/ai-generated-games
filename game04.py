# Write a Pygame tic-tac-toe game:
import pygame
import sys
import time
import random

blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

bg = pygame.image.load("tictacbg.png")
x = pygame.image.load("x.png")
o = pygame.image.load("o.png")
x = pygame.transform.scale(x, (100, 100))
o = pygame.transform.scale(o, (100, 100))

pygame.init()
clock = pygame.time.Clock()

info = pygame.display.Info()
size = width, height = info.current_w/2, info.current_h/2

screen = pygame.display.set_mode(size) #, pygame.FULLSCREEN)

turn = random.randint(0, 1)

if turn == 0:
    pygame.display.set_caption("Player 1")
else:
    pygame.display.set_caption("Player 2")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def winner(board, mark):
    win_cond = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_cond:
        if board[each[0]] == board[each[1]] == board[each[2]] == mark:
            return True
        else:
            pass
    return False

def draw(board):
    pygame.draw.line(screen, blue, (100, 0), (100, 900), 7)
    pygame.draw.line(screen, blue, (200, 0), (200, 900), 7)
    pygame.draw.line(screen, blue, (0, 100), (900, 100), 7)
    pygame.draw.line(screen, blue, (0, 200), (900, 200), 7)
    for i in range(3):
        for j in range(3):
            if board[i*3 + j] == 'x':
                screen.blit(x, (j*300, i*300))
            elif board[i*3 + j] == 'o':
                screen.blit(o, (j*300, i*300))

    pygame.display.update()

def game_loop():
    global turn
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg, (0, 0))

        mx, my = pygame.mouse.get_pos()

        button = pygame.Rect(0, 0, width, height)

        if button.collidepoint((mx, my)):
            if turn == 0:
                pygame.draw.rect(screen, red, button)
                if pygame.mouse.get_pressed()[0]:
                    pos = ((mx//300)*3 + my//300)
                    board[pos] = 'x'

                    if winner(board, 'x'):
                        message_display('Player 1 Wins!')
                    draw(board)
                    turn = 1
                    pygame.display.set_caption("Player 2")
            else:
                pygame.draw.rect(screen, red, button)
                if pygame.mouse.get_pressed()[0]:
                    pos = ((mx//300)*3 + my//300)
                    board[pos] = 'o'

                    if winner(board, 'o'):
                        message_display('Player 2 Wins!')
                    draw(board)
                    turn = 0
                    pygame.display.set_caption("Player 1")

        clock.tick(60)

board = [' ' for x in range(9)]

game_loop()