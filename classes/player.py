class Player:
    def __init__(self, name, initials, row, col, team, board):
        self.name = name
        self.initials = initials
        self.row = row
        self.col = col
        self.team = team
        self.board = board
        self.board.board[row][col].set_player(self)

    def move(self, steps):
        pass

    def change_possition(self, new_row, new_col):
        board.board[self.row][self.col].remove_player()
        self.row = new_row
        self.col = new_col
        board.board[self.row][self.col].set_player(self)

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
