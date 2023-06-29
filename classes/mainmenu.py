import pygame
import pickle
import os
from classes.JK_library import Colors
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

        # self.save_board("save_board_")

    def load_board(self):
        self.board = Board(400, 25)
        self.board.generate()
        # Load the object from the file
        # with open('my_object.pickle', 'rb') as file:
        #     loaded_object = pickle.load(file)

    # Verify that the loaded object is the same as the original
    # def verify_load_board(self):
    #     assert my_object == loaded_object

    # Save the object to a file
    def save_board(self, file):
        save_file = self.create_next_version("/saves", file)
        with open(save_file, 'wb') as save_file:
            pickle.dump(self.board, save_file)

    # Create next version filename for save
    def create_next_version(self, path, key):
        # Get a list of files in the directory
        files = os.listdir(path)

        # Initialize the version counter
        version = 0

        # Iterate through all files in the directory
        for file in files:
            # If the file matches the key
            if file.startswith(key):
                # Extract the version number from the file name
                file_version = int(file[len(key):-4])
                # Update the version counter
                version = max(version, file_version + 1)

        # Create the name for the new file
        new_file = f"{key}{version:03d}.sav"

        # Create the new file
        with open(os.path.join(path, new_file), 'w') as file:
            pass

        # Return the name of the new file
        return new_file

    def load_teams(self):
        self.teams.update({"AJK": Team("AJK", "aJKa software", Colors.PINK)})
        self.teams.update({"SPA": Team("SPA", "Spain", Colors.YELLOW)})
        self.teams.update({"GBP": Team("GBP", "Great Britain", Colors.RED)})
        self.teams.update({"FRN": Team("FRN", "France", Colors.BLUE)})
        self.teams.update({"COL": Team("COL", "Columbia", Colors.ORANGE)})

    def load_players(self):
        self.players.append(Player("Petr Vakoč", "PV", 0, 0, self.teams["AJK"], self.board))
        self.players.append(Player("Zdeněk Štybar", "ZS", 0, 0, self.teams["AJK"], self.board))
        self.players.append(Player("Roman Kreuziger", "RK", 0, 0, self.teams["AJK"], self.board))
        self.players.append(Player("Michal Kwiatkowski", "MK", 0, 0, self.teams["AJK"], self.board))
        self.players.append(Player("Jan Hirt", "JH", 0, 0, self.teams["AJK"], self.board))
        self.players.append(Player("Josef Černý", "JC", 0, 0, self.teams["AJK"], self.board))

        # Tým SPA (Spain)
        self.players.append(Player("Alejandro Valverde", "AV", 0, 0, self.teams["SPA"], self.board))
        self.players.append(Player("Mikel Landa", "ML", 0, 0, self.teams["SPA"], self.board))
        self.players.append(Player("Enric Mas", "EM", 0, 0, self.teams["SPA"], self.board))
        self.players.append(Player("Ion Izagirre", "II", 0, 0, self.teams["SPA"], self.board))
        self.players.append(Player("Marc Soler", "MS", 0, 0, self.teams["SPA"], self.board))
        self.players.append(Player("David de la Cruz", "DC", 0, 0, self.teams["SPA"], self.board))

        # Tým GBP (Great Britain)
        self.players.append(Player("Chris Froome", "CF", 0, 0, self.teams["GBP"], self.board))
        self.players.append(Player("Geraint Thomas", "GT", 0, 0, self.teams["GBP"], self.board))
        self.players.append(Player("Adam Yates", "AY", 0, 0, self.teams["GBP"], self.board))
        self.players.append(Player("Simon Yates", "SY", 0, 0, self.teams["GBP"], self.board))
        self.players.append(Player("Mark Cavendish", "MC", 0, 0, self.teams["GBP"], self.board))
        self.players.append(Player("Tom Pidcock", "TP", 0, 0, self.teams["GBP"], self.board))

        # Team FRN (France)
        self.players.append(Player("Julian Alaphilippe", "JA", 0, 0, self.teams["FRN"], self.board))
        self.players.append(Player("Thibaut Pinot", "TP", 0, 0, self.teams["FRN"], self.board))
        self.players.append(Player("Romain Bardet", "RB", 0, 0, self.teams["FRN"], self.board))
        self.players.append(Player("Arnaud Démare", "AD", 0, 0, self.teams["FRN"], self.board))
        self.players.append(Player("David Gaudu", "DG", 0, 0, self.teams["FRN"], self.board))
        self.players.append(Player("Guillaume Martin", "GM", 0, 0, self.teams["FRN"], self.board))

        # Team COL (Columbia)
        self.players.append(Player("Egan Bernal", "EB", 0, 0, self.teams["COL"], self.board))
        self.players.append(Player("Nairo Quintana", "NQ", 0, 0, self.teams["COL"], self.board))
        self.players.append(Player("Rigoberto Uran", "RU", 0, 0, self.teams["COL"], self.board))
        self.players.append(Player("Esteban Chaves", "EC", 0, 0, self.teams["COL"], self.board))
        self.players.append(Player("Miguel Angel Lopez", "MAL", 0, 0, self.teams["COL"], self.board))
        self.players.append(Player("Ivan Sosa", "IS", 0, 0, self.teams["COL"], self.board))
