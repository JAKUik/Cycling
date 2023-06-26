import random
from .field import Field
from .JK_library import *

class Board:
    """
    Game board
    :param rows:
    :param columns: Will be increase to even
    """
    def __init__(self, rows, columns):
        self.board = []
        self.rows = rows
        self.columns = columns + columns % 2  # Increase to even
        self.generate()
        # Create a empty game board
        # for i in range(self.rows):
        #     r = []
        #     for j in range(self.columns):
        #         # Temporary ... will be generated with route and other
        #         if 2 < j < 7:
        #             r.append(Field(i, j, LIGHT_GRAY, True))
        #         elif j == 2 or j == 7:
        #             r.append(Field(i, j, DARK_GRAY, False))
        #         else:
        #             r.append(Field(i, j, DARK_GREEN, False))
        #     self.board.append(r)

    def generate(self):
        max_width = 5
        min_width = 2
        width_way = 5
        last_width_way = width_way
        left_border = (self.columns - width_way) // 2
        right_border = left_border + width_way + 1
        direction = 0
        min_sector = 6
        i = 0
        while i < self.rows:
            # if i < self.rows - 9:
            sector_length = random.randint(min_sector, 10)
            for j in range(sector_length):
                # Generating 1 line. Change border.
                r, left_border, right_border, direction = \
                    self.generate_one_line(i, left_border, right_border, direction, width_way)
                self.board.append(r)
                i += 1
                if i >= self.rows:
                    break
            direction = random.randint(-1, 1)
            width_way += random.randint(-1, 1)
            width_way = max(min(width_way, max_width), min_width)

    def generate_one_line(self, row, left_border, right_border, direction, width_way):
        if left_border < 1:
            direction = 1
        elif right_border > self.columns - 2:
            direction = -1
        # Generating 1 row
        r = []
        if width_way > right_border - left_border - 1:
            left_border = self.next_column(row, left_border, -1)
            right_border = self.next_column(row, right_border, 1)
        elif width_way < right_border - left_border - 1:
            left_border = self.next_column(row, left_border, 1)
            right_border = self.next_column(row, right_border, -1)
        else:  # We can apply direction
            if direction < 0:
                left_border = self.next_column(row, left_border, -1)
                right_border = self.next_column(row, right_border, -1)
            elif direction > 0:
                left_border = self.next_column(row, left_border, 1)
                right_border = self.next_column(row, right_border, 1)
            else:
                left_border = self.next_column(row, left_border, 0)
                right_border = self.next_column(row, right_border, 0)
        # Create list with 1 line
        for c in range(self.columns):
            if left_border == c or right_border == c:
                r.append(Field(row, c, DARK_GRAY, False))
            elif left_border < c < right_border:
                r.append(Field(row, c, LIGHT_GRAY, True))
            else:
                r.append(Field(row, c, DARK_GREEN, False))
        return r, left_border, right_border, direction

    def next_column(self, row, col, direction):
        row += 1
        if direction == 1:
            return col + row % 2
        elif direction == -1:
            return col + (row % 2) - 1
        return col


    def field(self, row, col):
        return self.board[row][col]

    def field_player(self, row, col):
        return self.board[row][col].player

    def field_enable(self, row, col):
        return self.board[row][col].enable

    def field_restore_bg(self, restore_list):
        for rc in restore_list:
            row, col = rc
            self.board[row][col].bg_color = self.board[row][col].bg_color_ini


