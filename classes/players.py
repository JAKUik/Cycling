import pygame

from classes.dice import Dice

KEY_MAIN_DICE = pygame.K_m
KEY_BREAK_DICE = 'B'
KEY_SPRINT_DICE = 'S'


class Players:
    def __init__(self, players, teams, board, output):
        self.players = players
        self.teams = teams
        self.board = board
        self.output = output
        self.players_pointer = None
        self.last_group = 0
        self._player = None
        # Set Dices odds
        self.main_dice = Dice('2' * 20 + '3' * 40 + '4' * 20 + '5' * 20 + '6' * 20)
        self.sprint_dice = Dice('3' * 20 + '4' * 40 + '5' * 40 + '6' * 20)
        self.break_dice = Dice('1' * 40 + '2' * 40 + '3' * 40)
        # Temp variables

    # TODO - Toto je asi špatně v logice
    def player_move(self):
        if self._player is None:
            # New player for move
            self._player = self.players[self.players_pointer]
            if self.last_group != self._player.group:
                # TODO - Select Dice (main or break)
                self._player.roll = self.main_dice.dice_roll()
                atp = self.board.get_accessible_target_positions(self._player.row, self._player.col, self._player.roll)
                print(self._player.roll, atp)

    def dice_roll(self, event_key):
        """
        Testing a possible dice actions and doing it
        :param event_key: Pressed key event
        """
        def after_dice_roll():
            self._player.main_dice = False
            self._player.break_dice = False
            self._player.take_roll = None
            accessible_fields = self.board.get_accessible_target_positions(
                self._player.row, self._player.col, self._player.roll if self._player.roll <4 else self._player.roll - 1)
            x = 1
            for r, c in accessible_fields:
                self.board.field(r, c).set_accessible_for_player_move(x)
                x += 1
            # Fills the roll for the rest of the group
            g = self._player.group
            for i in range(self.players_pointer, len(self.players)):
                if g == self.players[i].group:
                    self.players[i].take_roll = self._player.roll
                else:
                    break
            self.output.draw_game_board()

        # ... dice_roll method continue
        if event_key == KEY_MAIN_DICE and self._player.main_dice:
            self._player.roll = self.main_dice.dice_roll()
            after_dice_roll()
        elif event_key == KEY_BREAK_DICE and self._player.break_dice:
            self._player.roll = self.break_dice.dice_roll()
            after_dice_roll()

    def new_round_reset_all_players(self):
        for player in self.players:
            player.new_round_reset()
        self.assign_players_order()
        self.set_groups()
        # Sorted all players by GROUP, ROW, COLUMN (front free fields = 2 or 1)
        self.players = sorted(self.players, key=lambda x: (x.group, -x.row, -x.front_enable, x.col))
        self.players_pointer = 0

    def assign_players_order(self):
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



