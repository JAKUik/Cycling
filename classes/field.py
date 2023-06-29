class Field:
    def __init__(self, row, col, bg_color, enable):
        self.row = row
        self.col = col
        self.bg_color_ini = bg_color
        self.bg_color = bg_color
        self.enable = enable
        self.player = None  # Player or None if field is free
        self.typ = "UP"  # UP DOWN PLAIN
        self.wind = "FRONT"  # FRONT BACK SIDE
        self.color = None
        # For save last possition on output
        self.x = None
        self.y = None
        self.width = None
        self.heigth = None

        self.print_console_value = f"{row:02}{col}"

    def is_accessible(self):
        return self.enable and not self.has_player()

    def set_player(self, player):
        self.player = player
        self.player.row = self.row
        self.player.col = self.col

    def remove_player(self):
        self.player.row = 0
        self.player.col = 0
        self.player = None

    def has_player(self):
        return self.player is not None
