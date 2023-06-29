import random

import pygame
CLOCK_TICK = 30


class GameLoop:
    def __init__(self, output, board, players, teams):
        self.board = board
        self.players = players
        self.teams = teams
        self.output = output
        self.starting_lineup()

    def main_loop(self):
        running = True
        action = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEWHEEL:
                    if event.y > 0:
                        self.output.scroll_game_board(-50)
                        action = True
                    elif event.y < 0:
                        self.output.scroll_game_board(50)
                        action = True
                if event.type == pygame.KEYDOWN:
                    pass
                    # print(event.type)
                    # if event.key == pygame.K_PAGEUP:
                    #     self.output.scroll_game_board(-400)
                    #     action = True
                    # elif event.key == pygame.K_PAGEDOWN:
                    #     self.output.scroll_game_board(400)
                    #     action = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.output.scroll_game_board(-CLOCK_TICK / 2)
                action = True
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.output.scroll_game_board(CLOCK_TICK / 2)
                action = True
            elif keys[pygame.K_PAGEUP]:
                self.output.scroll_game_board(-400)
                action = True
            elif keys[pygame.K_PAGEDOWN]:
                self.output.scroll_game_board(400)
                action = True

            # Draw the screen after the action
            if action:
                self.output.draw_game_board()
                action = False

            pygame.display.update()

            self.output.clock.tick(CLOCK_TICK)

    # The players' line-up at the start
    def starting_lineup(self):
        random.shuffle(self.players)
        p = 0
        for i in range(self.board.rows):
            for j in range(self.board.columns):
                if self.board.field(i, j).enable:
                    self.board.field(i, j).set_player = self.players[p]
                    # print(f"{i}, {j}, {p}, ")
                    # print(f"{self.board[i][j].player.row} - {self.board[i][j].player.col}")

                    p += 1
                    if p >= len(self.players):
                        return  # Pěkně divné řešení !!!


