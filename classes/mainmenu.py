import pygame
import pickle
import os
from classes.JK_library import Colors
from classes.board import Board
from classes.gameloop import GameLoop
from view_modules.viewboard import ViewBoard
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
        self.output = ViewBoard(screen_widht, screen_height, self.board)
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
        self.players.append(Player("Petr Vakoč", "PV", self.teams["AJK"]))
        self.players.append(Player("Zdeněk Štybar", "ZS", self.teams["AJK"]))
        self.players.append(Player("Roman Kreuziger", "RK", self.teams["AJK"]))
        self.players.append(Player("Michal Kwiatkowski", "MK", self.teams["AJK"]))
        self.players.append(Player("Jan Hirt", "JH", self.teams["AJK"]))
        self.players.append(Player("Josef Černý", "JC", self.teams["AJK"]))

        # Tým SPA (Spain))
        self.players.append(Player("Alejandro Valverde", "AV", self.teams["SPA"]))
        self.players.append(Player("Mikel Landa", "ML", self.teams["SPA"]))
        self.players.append(Player("Enric Mas", "EM", self.teams["SPA"]))
        self.players.append(Player("Ion Izagirre", "II", self.teams["SPA"]))
        self.players.append(Player("Marc Soler", "MS", self.teams["SPA"]))
        self.players.append(Player("David de la Cruz", "DC", self.teams["SPA"]))

        # Tým GBP (Great Britain))
        self.players.append(Player("Chris Froome", "CF", self.teams["GBP"]))
        self.players.append(Player("Geraint Thomas", "GT", self.teams["GBP"]))
        self.players.append(Player("Adam Yates", "AY", self.teams["GBP"]))
        self.players.append(Player("Simon Yates", "SY", self.teams["GBP"]))
        self.players.append(Player("Mark Cavendish", "MC", self.teams["GBP"]))
        self.players.append(Player("Tom Pidcock", "TP", self.teams["GBP"]))

        # Team FRN (France))
        self.players.append(Player("Julian Alaphilippe", "JA", self.teams["FRN"]))
        self.players.append(Player("Thibaut Pinot", "TP", self.teams["FRN"]))
        self.players.append(Player("Romain Bardet", "RB", self.teams["FRN"]))
        self.players.append(Player("Arnaud Démare", "AD", self.teams["FRN"]))
        self.players.append(Player("David Gaudu", "DG", self.teams["FRN"]))
        self.players.append(Player("Guillaume Martin", "GM", self.teams["FRN"]))

        # Team COL (Columbia))
        self.players.append(Player("Egan Bernal", "EB", self.teams["COL"]))
        self.players.append(Player("Nairo Quintana", "NQ", self.teams["COL"]))
        self.players.append(Player("Rigoberto Uran", "RU", self.teams["COL"]))
        self.players.append(Player("Esteban Chaves", "EC", self.teams["COL"]))
        self.players.append(Player("Miguel Angel Lopez", "MAL", self.teams["COL"]))
        self.players.append(Player("Ivan Sosa", "IS", self.teams["COL"]))
