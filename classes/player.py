class Player:
    def __init__(self, name, monogram, team):
        self.name = name
        self.monogram = monogram
        self.row = None  # Row on the board
        self.col = None  # Column on the board
        self.team = team
        self.group = None  # Group number for each round
        self.order = None  # Order for each round
        self.front_enable = None  # The number of available fields in front
        self.take_roll = None
        self.main_dice = None
        self.sprint_dice = None
        self.break_dice = None
        self.actual = False
        # self.fields_for_move = []

        # self.board = board
        # self.board.board[row][col].set_player(self)

    def new_round_reset(self):
        self.group = None
        self.order = None
        self.front_enable = None
        self.take_roll = None
        self.main_dice = True
        self.sprint_dice = False
        self.break_dice = True
        # self.fields_for_move = []



"""
    def move(self, steps):
        pass

    def change_possition(self, new_row, new_col):
        self.board[self.row][self.col].remove_player()
        self.row = new_row
        self.col = new_col
        self.board[self.row][self.col].set_player(self)

    def step(self, direction):
        # Implement your movement logic here
        if direction == "up":
            self.col -= 1
        elif direction == "down":
            self.col += 1
        elif direction == "left":
            self.row -= 1
        elif direction == "right":
            self.row += 1

        # Access other fields on the game board
        for row in self.board:
            for field in row:
                # Access field properties
                print(field.row, field.col, field.color, field.typ, field.wind)
"""