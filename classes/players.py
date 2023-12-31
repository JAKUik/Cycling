import pygame
import random

from view_modules.drawable import *
from classes.dice import Dice
from classes.JK_library import *

KEY_MAIN_DICE = pygame.K_m
KEY_BREAK_DICE = pygame.K_b
KEY_SPRINT_DICE = pygame.K_s


class Players:
    def __init__(self, players, teams, board, output):
        self.players = players
        self._players = []  # List for one round
        self.teams = teams
        self.board = board
        self.output = output
        self._players_pointer = None
        self.last_group = 0
        self._player = None
        # Set Dices odds
        self.main_dice = Dice('2' * 20 + '3' * 40 + '4' * 20 + '5' * 20 + '6' * 20)
        self.sprint_dice = Dice('3' * 20 + '4' * 40 + '5' * 40 + '6' * 20)
        self.break_dice = Dice('1' * 40 + '2' * 40 + '3' * 40)
        # Temp variables
        self.accessible_fields = None
        self.roll = 0
        self.escape = False

    def update_info_panel_items(self):
        # f = self.board.field(self._player.row, self._player.col)
        # if f.height is not None:
        #     self.output.border_hexagon(f.x, f.y, f.width, f.height, Colors.BLACK, 10)
        #     self.output.draw_game_board()

        if self._player.main_dice:
            self.output.info_container.add_new_item\
                ("main_dice", DrawText(self.output.info_container.info_panel, (10, 60), f"Chose MAIN dice: (M)", 25,
                                       Colors.BLACK))
        else:
            self.output.info_container.info_panel.surface.fill(Colors.YELLOW)
            self.output.info_container.remove_item("main_dice")
        if self._player.break_dice:
            self.output.info_container.add_new_item(
                "break_dice", DrawText(self.output.info_container.info_panel, (10, 90), f"Chose BREAK dice: (B)",
                                       25, Colors.BLACK))
        else:
            self.output.info_container.info_panel.surface.fill(Colors.YELLOW)
            self.output.info_container.remove_item("break_dice")
        if self._player.sprint_dice:
            self.output.info_container.add_new_item(
                "sprint_dice", DrawText(self.output.info_container.info_panel, (10, 120), f"Chose SPRINT dice: (S)",
                                        25, Colors.BLACK))
        else:
            self.output.info_container.info_panel.surface.fill(Colors.YELLOW)
            self.output.info_container.remove_item("sprint_dice")
        if self._player.take_roll is not None:
            self.output.info_container.add_new_item(
                "assume", DrawText(self.output.info_container.info_panel, (10, 150),
                                   f"Roll / Assume: {self.roll} / {self._player.take_roll}", 25, Colors.BLACK))

        self.output.info_container.add_new_item(
            "rider", DrawText(self.output.info_container.info_panel, (10, 200), "Rider:", 30, Colors.BLACK))
        self.output.info_container.add_new_item(
            "rider_data", DrawList(self.output.info_container.info_panel, (10, 230),
                                   f"Name:   {self._player.name}\n"
                                   f"Team:   {self._player.team.name}", 25, Colors.BLACK))

    def player_move(self, event_key):

        if self.accessible_fields is None:
            return False  # Player isn't ready for move

        if event_key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6,
                         pygame.K_7, pygame.K_8, pygame.K_9]:
            index = event_key - pygame.K_1
        elif event_key in [pygame.K_KP_1, pygame.K_KP_2, pygame.K_KP_3, pygame.K_KP_4, pygame.K_KP_5, pygame.K_KP_6,
                           pygame.K_KP_7, pygame.K_KP_8, pygame.K_KP_9]:
            index = event_key - pygame.K_KP_1
        else:
            return False

        if index < len(self.accessible_fields):
            self.board.field(self._player.row, self._player.col).remove_player()
            self.board.field(self.accessible_fields[index][0], self.accessible_fields[index][1])\
                .set_player(self._player)
            self.clear_accessible_fields_from_board()
            self.accessible_fields = []
            if self.roll == 2 and self._player.sprint_dice:
                self.escape = True  # The player has moved himself
                return True
            self.next_player(True)
            return True

    def dice_roll(self, event_key):
        """
        Testing a possible dice actions and doing it
        :param event_key: Pressed key event
        """
        def after_dice_roll(dice):  # This is inside function
            self._player.main_dice = False
            self._player.break_dice = False
            self._player.sprint_dice = self.roll == 2 and dice == "MAIN" \
                and self.isnt_alone(self._player.row, self._player.col, self._players)
            self._player.take_roll = None
            self.set_groups()
            # Set break_dice for next two players
            if dice == "BREAK":
                g = self._player.group
                for i in range(1, 3):
                    if self._players_pointer + i >= len(self._players) or g != self._players[i].group:
                        break
                    else:
                        self._players[i].main_dice = False
            if dice != "SPRINT":
                m = self.roll if self.roll < 4 else self.roll - 1
            else:
                if self.escape:  # Samostatný únik
                    print(f"Sprint únik. SPRINT dice: {self.roll}")
                    m = self.roll
                    self.roll = None
                else:
                    print(f"Sprint skupina.SPRINT dice: {self.roll} + 2")
                    self.roll += 2  # Group take 2 + sprint.dice
                    m = self.roll
                # když SPRINT sám tak self.roll = None
                # jinak self.roll = 2 + self.roll
            if self.accessible_fields:
                self.clear_accessible_fields_from_board()
            self.create_accessible_fields(self._player.row, self._player.col, m, dice)
            # Fills the roll for the rest of the group
            g = self._player.group
            for i in range(self._players_pointer, len(self._players)):
                if g == self._players[i].group:
                    self._players[i].take_roll = self.roll
                else:
                    break
            # self.output.draw_game_board()

        # ... dice_roll method continue
        if event_key == KEY_MAIN_DICE and self._player.main_dice:
            print("Hlavní kostka")
            self.roll = self.main_dice.dice_roll()
            after_dice_roll("MAIN")
            return True
        if event_key == KEY_BREAK_DICE and self._player.break_dice:
            print("Brzdící kostka")
            self.roll = self.break_dice.dice_roll()
            after_dice_roll("BREAK")
            return True
        if event_key == KEY_SPRINT_DICE and self._player.sprint_dice:
            print("Sprint kostka")
            self.roll = self.sprint_dice.dice_roll()
            after_dice_roll("SPRINT")
            return True

    def is_next_player(self):
        return self._players_pointer + 1 < len(self._players)

    def next_player(self, can_player_takes_roll):
        self.escape = False
        last_group = self._player.group
        self._player.actual = False
        self._players.pop(0)
        if self._players_pointer >= len(self._players):
            self._players_pointer = None
            return True
        self._player = self._players[self._players_pointer]
        self._player.actual = True
        if last_group == self._player.group and can_player_takes_roll:  # CHECK - Zřejmě to jde udělat i bez can_player...
            self.create_accessible_fields(self._player.row, self._player.col, self._player.take_roll)
        return True

    def isnt_alone(self, row, col, _players):
        """
        :param row:
        :param col:
        :param _players: Remaining player on this round
        :return: True - If someone on surrounding positions
        """
        sp = self.board.surrounding_positions(row, col)
        for r, c in sp:
            for p in _players:
                if p.row == r and p.col == c:
                    return True
        return False

    def create_accessible_fields(self, r, c, m, dice="MAIN"):
        self.accessible_fields = self.board.get_accessible_target_positions(r, c, m)
        # if len(self.accessible_fields) == 0:  # One more time, but slower
        if dice != "BREAK":
            self.accessible_fields += self.board.get_accessible_target_positions(r, c, m - 1)
        if len(self.accessible_fields) == 0 and not self._player.break_dice:  # The cyclist fell
            print("JEZDEC UPADL")
            self.next_player(True)
        self.set_accessible_fields_to_board()

    def set_accessible_fields_to_board(self):
        x = 1
        for r, c in self.accessible_fields:
            self.board.field(r, c).set_accessible_for_player_move(x)
            x += 1

    def clear_accessible_fields_from_board(self):
        for r, c in self.accessible_fields:
            self.board.field(r, c).set_accessible_for_player_move(None)

    def new_round_reset_all_players(self):
        self._players = self.players.copy()
        for player in self._players:
            player.new_round_reset()
        self.assign_players_order()
        self.set_groups()
        # Sorted all players by GROUP, ROW, COLUMN (front free fields = 2 or 1)
        self._players = sorted(self._players, key=lambda x: (x.group, -x.row, -x.front_enable, x.col))
        self._players_pointer = 0
        self._player = self._players[self._players_pointer]
        self._player.actual = True

    def assign_players_order(self):
        """
        Sorts the list of players for the new round
        """
        for player in self._players:
            player.front_enable = self.board.count_front_enable(player.row, player.col)
        self._players = sorted(self._players, key=lambda x: (-x.row, -x.front_enable, x.col))
        order = 1
        for player in self._players:
            player.order = order
            order += 1

    def set_groups(self):
        """
        Sets all groups for all players to one round
        """
        for player in self._players:
            player.group = None
        group_number = 1
        for player in self._players:
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
        # Nefunční AI
        # NEFUNKČNÍ AI
        # group_number = 1
        # for player in self._players:
        #     if player.group is None:
        #         player.group = group_number
        #     if player.row % 2 == 0:
        #         adjacent_positions = [(player.row + 1, player.col), (player.row + 1, player.col - 1)]
        #     else:
        #         adjacent_positions = [(player.row + 1, player.col + 1), (player.row + 1, player.col)]
        #     for row, col in adjacent_positions:
        #         for p in self._players:
        #             if p.row == row and p.col == col and p.group is None:
        #                 p.group = player.group
        #     group_number += 1

    def starting_lineup(self):
        """
        Line-up all players at the start
        """
        random.shuffle(self.players)
        p = 0
        for i in range(self.board.rows):
            # TEMP vytvoření skupin
            # if i % 2 == 1:
            #     continue
            # ####################
            for j in range(self.board.columns):
                if self.board.field(i, j).enable:
                    self.board.field(i, j).set_player(self.players[p])
                    p += 1
                    if p >= len(self.players):
                        return  # TODO: Opravdu ukončovat smyčku returnem ?



