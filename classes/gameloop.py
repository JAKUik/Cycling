import pygame
from classes.players import Players
CLOCK_TICK = 30


class GameLoop:
    def __init__(self, output, board, players, teams):
        """
        The MAIN game object
        :param output: The output module
        :param board: The game board with the way
        :param players: The list of all plaing players
        :param teams: All teams for players
        """
        self.board = board
        # self.players = players
        self.players = Players(players, teams, board, output)
        # self.players_pointer = None
        self.teams = teams
        self.output = output
        self.refresh_board = True
        # For each round
        self.round = 0
        # Fro each player
        # self._player = None
        # self.roll = None

        self.players.starting_lineup()

    def main_loop(self):
        """
        The loop for one game from the start to the finish
        """
        clock = pygame.time.Clock()
        running = True
        self.refresh_board = True

        while running:
            if self.players.players_pointer is None:
                self.new_round()

            # # CHECK Tady nebo jinde ?
            # self.players.check_new_player()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEWHEEL:
                    if event.y > 0:
                        self.output.scroll_game_board(-50)
                        self.refresh_board = True
                    elif event.y < 0:
                        self.output.scroll_game_board(50)
                        self.refresh_board = True
                if event.type == pygame.KEYDOWN:
                    # Testing all possible actions with dice
                    self.refresh_board = self.players.dice_roll(event.key) or self.refresh_board
                    self.refresh_board = self.players.player_move(event.key) or self.refresh_board

                    # if index < len():
                    #     pass
                    # print(event.type)
                    # if event.key == pygame.K_PAGEUP:
                    #     self.output.scroll_game_board(-400)
                    #     self.refresh_board = True
                    # elif event.key == pygame.K_PAGEDOWN:
                    #     self.output.scroll_game_board(400)
                    #     self.refresh_board = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            # elif keys[pygame.K_UP] or keys[pygame.K_w]:
            #     self.output.scroll_game_board(-CLOCK_TICK / 2)
            #     self.refresh_board = True
            # elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            #     self.output.scroll_game_board(CLOCK_TICK / 2)
            #     self.refresh_board = True
            elif keys[pygame.K_PAGEUP]:
                self.output.scroll_game_board(-400)
                self.refresh_board = True
            elif keys[pygame.K_PAGEDOWN]:
                self.output.scroll_game_board(400)
                self.refresh_board = True



            # Draw the screen after the self.refresh_board
            if self.refresh_board:
                self.output.draw_game_board()
                self.refresh_board = False

            pygame.display.update()
            clock.tick(CLOCK_TICK)

    def new_round(self):
        self.round += 1
        self.players.new_round_reset_all_players()
        self.refresh_board = True


