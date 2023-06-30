import pygame
from classes.JK_library import *
from classes.container import Container


class ViewModule:
    def __init__(self, window_width, window_height, game_board):
        self.window_width = window_width
        self.window_height = window_height
        self.game_board = game_board
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Cycling")
        # Set white background
        self.background_color = Colors.LIGHT_GRAY
        # self.screen.fill(self.background_color)

        # TODO - Optimalizate the hexagon width and height
        self.font = pygame.font.Font(None, 20)
        # Calculate the dimensions of the hexagon
        self.hexagon_width = self.window_width // 35
        self.hexagon_height = int(self.hexagon_width * 1)

        self.board_contaniner = Container(10, 0, self.window_width // 4 * 3, self.hexagon_height
                                          * self.game_board.rows * 0.75 + 10, self.screen)
        self.board_contaniner.surface.fill(Colors.DARK_GREEN)

    def draw_game_board(self):
        # Iterate over the game board and draw the fields
        self.screen.fill(self.background_color)
        for row_idx in range(len(self.game_board.board) - 1, -1, -1):
            x = self.game_board.board[row_idx]
            for col_idx, field in enumerate(x):
                x = self.hexagon_width * col_idx + (self.hexagon_width // 2) * (row_idx % 2)
                y = self.hexagon_height * (len(self.game_board.board) - row_idx - 1) * 0.75
                self.draw_field(field, x, y, self.hexagon_width, self.hexagon_height)
                #
                # Maybe here I can check the integrity controls (etc. only one possition on player ...)
                #
        pygame.display.flip()
        self.calculate_x_for_row(10)
        # self.board_contaniner.draw(self.screen)
        self.draw_container(self.board_contaniner, self.screen)

    def draw_field(self, field, x=None, y=None, width=None, height=None):
        """
        Draw one hexagon field to possition x,y with width and height
        Save x,y, width and height to Field attributs
        :param field:
        :param x: if is None fill it by field.x (last draw possition)
        :param y:
        :param width:
        :param height:
        :return:
        """
        x = field.x if x is None else x
        y = field.y if y is None else y
        width = field.width if width is None else width
        height = field.heigth if height is None else width

        bg = field.bg_color
        if field.player is not None:
            bg = field.player.team.color
        self.draw_one_hexagon(x, y, width, height, bg, Colors.BLACK)


        # Render the field's coordinates as text
        if not field.enable:
            # Blit the text onto the surface
            text = self.font.render(f"{field.row},{field.col}", True, Colors.BLACK)
            text_rect = text.get_rect(center=(x + width / 2, y + height / 2))
            self.board_contaniner.surface.blit(text, text_rect)
        elif field.has_player():
            # TEMP !!!
            text = self.font.render(f"{field.player.group}/{field.player.order}", True, Colors.BLACK)
            # text = self.font.render(f"{field.player.monogram}", True, Colors.BLACK)
            text_rect = text.get_rect(center=(x + width / 2, y + height / 2))
            self.board_contaniner.surface.blit(text, text_rect)
        # elif  TODO Vykreslení pozice na kterou může hráč vstoupit
            
        # Render Player
        #
        #

    def draw_one_hexagon(self, x, y, width, height, fill_color, border_color):
        pygame.draw.polygon(self.board_contaniner.surface, fill_color, [
            (x, y + height // 4),
            (x + width // 2, y),
            (x + width, y + height // 4),
            (x + width, y + 3 * height // 4),
            (x + width // 2, y + height),
            (x, y + 3 * height // 4)
        ])

        # Draw the black outline of the hexagon
        pygame.draw.polygon(self.board_contaniner.surface, border_color, [
            (x, y + height // 4),
            (x + width // 2, y),
            (x + width, y + height // 4),
            (x + width, y + 3 * height // 4),
            (x + width // 2, y + height),
            (x, y + 3 * height // 4)
        ], 1)  # The third argument (1) specifies the line thickness




    def scroll_game_board(self, dy):
        self.board_contaniner.scroll(0, dy)

    def calculate_x_for_row(self, row):
        # self.hexagon_height
        # self.game_board.board.rows
        # Calculate rows on the screen
        min_rows = self.window_height // (self.hexagon_height * 0.75) - 1
        row = max(min_rows, row)
        self.board_contaniner.set_position(None, -self.hexagon_height * self.game_board.rows * 0.75 + (row + 1)
                                           * self.hexagon_height * 0.75)
        # self.board_contaniner.set_position(None, -self.hexagon_height * self.game_board.rows)

    @staticmethod
    def draw_container(container, screen):
        screen.blit(container.surface, (container.x - container.scroll_x, container.y - container.scroll_y))
