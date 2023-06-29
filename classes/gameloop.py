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
        self.round = 0
        self.groups = []

    def main_loop(self):
        running = True
        action = True
        self.new_round()
        # self.output.draw_game_board()
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

    def new_round(self):
        """
        New round
        """
        self.round += 1
        for player in self.players:
            player.order = None
            player.group = None
            player.front_enable = None
        self.assign_player_order()
        self.output.draw_game_board()
        self.set_groups()
        self.players = sorted(self.players, key=lambda x: (x.group, -x.row, -x.front_enable, x.col))
        self.output.draw_game_board()
        pass

    def assign_player_order(self):
        """
        Sorts players for a new round
        :return:
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
        Sets groups for all players for one round
        """
        group_number = 1  # TODO: Dodělat
        for player in self.players:
            if player.group is None:
                self.search_group_members(player, group_number)
                group_number += 1

    def search_group_members(self, player, group_number):
        player.group = group_number
        field_around = self.board.surrounding_positions(player.row, player.col)
        for r, c in field_around:
            field = self.board.field(r, c)
            print(f"{field.player}")
            if field.player is not None and field.player.group is None:
                self.search_group_members(field.player, group_number)


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

    # The players' line-up at the start
    def starting_lineup(self):
        """
        Line-up all players at the start
        """
        # random.shuffle(self.players)  ## TEMP
        p = 0
        for i in range(self.board.rows):
            # TEMP vytvoření skupin
            if i % 2 == 1:
                continue
            for j in range(self.board.columns):
                if self.board.field(i, j).enable:
                    self.board.field(i, j).set_player(self.players[p])
                    p += 1
                    if p >= len(self.players):
                        return  # TODO: Opravdu ukončovat smyčku returnem ?


