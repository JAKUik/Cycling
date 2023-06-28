import pygame
from classes.JK_library import *
from classes.board import Board
from classes.gameloop import GameLoop
from classes.viewmodule import ViewModule
from classes.player import Player
from classes.team import Team


class MainMenu:
    def __init__(self):
        self.board = []
        self.teams = {}
        self.players = []
        self.output = None
        self.game = None

    def main_menu(self):
        display_info = pygame.display.get_desktop_sizes()
        display_resolution_x, display_resolution_y = display_info[0]
        # print(display_resolution_x, display_resolution_y)

        screen_widht = min(1600, display_resolution_x)
        screen_height = min(1200, display_resolution_y)

        self.load_board()
        self.load_teams()
        self.load_players()
        self.output = ViewModule(screen_widht, screen_height, self.board)
        self.game = GameLoop(self.output, self.board, self.players, self.teams)

        self.game.main_loop()

    def load_board(self):
        self.board = Board(400, 25)
        self.board.generate()

    def save_board(self):
        pass

    def load_teams(self):
        self.teams = {"AJK": Team("AJK", "aJKa software", PINK)}

    def load_players(self):
        self.players.append(Player("Béďa Ocásek", "BO", 0, 12, self.teams["AJK"], self.board))
        self.players.append(Player("Véna Fofrník", "VF", 0, 13, self.teams["AJK"], self.board))

