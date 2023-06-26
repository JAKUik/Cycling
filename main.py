from classes.JK_library import *
from classes.board import Board
from classes.player import Player
from classes.team import Team
from classes.gameoutput import GameOutput
from classes.game import Game

import pygame
pygame.init()

if __name__ == '__main__':
    pass

screen_widht = 1280
screen_height = 1024
clock_tick = 30

board = Board(400, 25)
output = GameOutput(screen_widht, screen_height, board)

players = list()

teams = {"AJK": Team("AJK", "aJKa software", PINK)}

players.append(Player("Béďa Ocásek", "BO", 0, 12, teams["AJK"], board))
players.append(Player("Véna Fofrník", "VF", 0, 13, teams["AJK"], board))

running = True
action = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                output.scroll_game_board(-50)
                action = True
            elif event.y < 0:
                output.scroll_game_board(50)
                action = True
        if event.type == pygame.KEYDOWN:
            pass
            # print(event.type)
            # if event.key == pygame.K_PAGEUP:
            #     output.scroll_game_board(-400)
            #     action = True
            # elif event.key == pygame.K_PAGEDOWN:
            #     output.scroll_game_board(400)
            #     action = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        output.scroll_game_board(-clock_tick / 2)
        action = True
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        output.scroll_game_board(clock_tick / 2)
        action = True
    elif keys[pygame.K_PAGEUP]:
        output.scroll_game_board(-400)
        action = True
    elif keys[pygame.K_PAGEDOWN]:
        output.scroll_game_board(400)
        action = True

    # Draw the screen after the action
    if action:
        output.draw_game_board()
        action = False

    pygame.display.update()

    output.clock.tick(clock_tick)


pygame.quit()
