import pygame
from classes.cube import Cube
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
        self.players = players
        self.players_pointer = None
        self.teams = teams
        self.output = output
        self.refresh_board = True
        # Set Cubes odds
        self.main_cube = Cube('2' * 20 + '3' * 40 + '4' * 20 + '5' * 20 + '6' * 20)
        self.sprint_cube = Cube('3' * 20 + '4' * 40 + '5' * 40 + '6' * 20)
        self.break_cube = Cube('1' * 40 + '2' * 40 + '3' * 40)
        # For each round
        self.round = 0
        self.groups = []
        self.last_group = 0
        # Fro each player
        self._player = None
        self.roll = None

        self.starting_lineup()

    def main_loop(self):
        """
        The loop for one game from the start to the finish
        """
        clock = pygame.time.Clock()
        running = True
        self.refresh_board = True
        self.new_round()
        # self.output.draw_game_board()
        while running:
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
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6,
                                     pygame.K_7, pygame.K_8, pygame.K_9]:
                        index = event.key - pygame.K_1
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

            # Player move
            self.player_move()

            # Draw the screen after the self.refresh_board
            if self.refresh_board:
                self.output.draw_game_board()
                self.refresh_board = False

            pygame.display.update()
# FIXME
            clock.tick(CLOCK_TICK)

    # TODO - Toto je asi špatně v logice
    def player_move(self):
        if self._player is None:
            # New player for move
            self._player = self.players[self.players_pointer]
            if self.last_group != self._player.group:
                # TODO - Select Cube (main or break)
                self.roll = self.main_cube.roll_dice()
                atp = self.board.get_accessible_target_positions(self._player.row, self._player.col, self.roll)
                print(self.roll, atp)

    def new_round(self):
        """
        New round
        """
        self.round += 1
        for player in self.players:
            player.new_round_reset()

        self.assign_player_order()
        self.set_groups()
        # Sorted all players by GROUP, ROW, COLUMN (front free fields = 2 or 1)
        self.players = sorted(self.players, key=lambda x: (x.group, -x.row, -x.front_enable, x.col))
        self.players_pointer = 0
        self.refresh_board = True

    def assign_player_order(self):
        """
        Sorts the list of players for the new round
        """
        for player in self.players:
            player.front_enable = self.board.count_front_enable(player.row, player.col)
        self.players = sorted(self.players, key=lambda x: (-x.row, -x.front_enable, x.col))
        order = 1
        for player in self.players:
            player.order = order
            order += 1

    def set_groups(self):
        """
        Sets all groups for all players to one round
        """
        group_number = 1
        for player in self.players:
            if player.group is None:
                self.search_group_members(player, group_number)
                group_number += 1

    def search_group_members(self, player, group_number):
        """
        Search and set one group
        :param player: First player in the group
        :param group_number: Number of group
        """
        player.group = group_number
        field_around = self.board.surrounding_positions(player.row, player.col)
        for r, c in field_around:
            field = self.board.field(r, c)
            if field.player is not None and field.player.group is None:
                self.search_group_members(field.player, group_number)

        # NEFUNKČNÍ AI
        # group_number = 1
        # for player in self.players:
        #     if player.group is None:
        #         player.group = group_number
        #     if player.row % 2 == 0:
        #         adjacent_positions = [(player.row + 1, player.col), (player.row + 1, player.col - 1)]
        #     else:
        #         adjacent_positions = [(player.row + 1, player.col + 1), (player.row + 1, player.col)]
        #     for row, col in adjacent_positions:
        #         for p in self.players:
        #             if p.row == row and p.col == col and p.group is None:
        #                 p.group = player.group
        #     group_number += 1

    def starting_lineup(self):
        """
        Line-up all players at the start
        """
        # random.shuffle(self.players)  ## TEMP - odstranit komentář
        p = 0
        for i in range(self.board.rows):
            # TODO - TEMP vytvoření skupin
            if i % 2 == 1:
                continue
            # ####################
            for j in range(self.board.columns):
                if self.board.field(i, j).enable:
                    self.board.field(i, j).set_player(self.players[p])
                    p += 1
                    if p >= len(self.players):
                        return  # TODO: Opravdu ukončovat smyčku returnem ?


