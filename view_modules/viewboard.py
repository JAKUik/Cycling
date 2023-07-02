import pygame
from classes.JK_library import *
from view_modules.container import Container
from view_modules.infopanel import InfoPanel


class ViewBoard:
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
        self.font40 = pygame.font.Font(None, 40)
        # Calculate the dimensions of the hexagon
        self.hexagon_width = self.window_width // 35
        self.hexagon_height = int(self.hexagon_width * 1)

        self.board_contaniner = Container(10, 0, self.window_width // 4 * 3, self.hexagon_height
                                          * self.game_board.rows * 0.75 + 10, self.screen)
        self.board_contaniner.surface.fill(Colors.DARK_GREEN)

        self.info_container = InfoPanel(self.board_contaniner.width, 0, self.window_width - self.board_contaniner.width,
                                        self.window_height, self.screen, Colors.YELLOW)

    def draw_game_board(self):
        # Iterate over the game board and draw the fields
        self.screen.fill(self.background_color)
        for row_idx in range(len(self.game_board.board) - 1, -1, -1):
            x = self.game_board.board[row_idx]
            for col_idx, field in enumerate(x):
                x = self.hexagon_width * col_idx + (self.hexagon_width // 2) * (row_idx % 2)
                y = self.hexagon_height * (len(self.game_board.board) - row_idx - 1) * 0.75
                self.draw_field(field, x, y, self.hexagon_width, self.hexagon_height)
        pygame.display.flip()
        self.calculate_x_for_row(10)
        self.draw_container(self.board_contaniner)

    def draw_info_panel(self):
        self.info_container.prepare_info_panel()
        self.draw_container(self.info_container.info_panel)

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
        if x is not None:
            field.x = x
        if y is not None:
            field.y = y
        if width is not None:
            field.width = width
        if height is not None:
            field.height = height

        bg = field.bg_color
        if field.player is not None:
            bg = field.player.team.color
        self.draw_one_hexagon(field.x, field.y, field.width, field.height, bg, Colors.BLACK)

        # Render the field's coordinates as text
        if not field.enable:
            # Blit the text onto the surface
            text = self.font.render(f"{field.row},{field.col}", True, Colors.BLACK)
            text_rect = text.get_rect(center=(field.x + field.width / 2, field.y + field.height / 2))
            self.board_contaniner.surface.blit(text, text_rect)
        elif field.accessible_for_move is not None:
            text = self.font40.render(f"{field.accessible_for_move}", True, Colors.PINK)
            text_rect = text.get_rect(center=(field.x + field.width / 2, field.y + field.height / 2))
            self.board_contaniner.surface.blit(text, text_rect)
        elif field.has_player():
            # TEMP !!!
            text = self.font.render(f"{field.player.group}/{field.player.order}", True, Colors.BLACK)
            # text = self.font.render(f"{field.player.monogram}", True, Colors.BLACK)
            text_rect = text.get_rect(center=(field.x + field.width / 2, field.y + field.height / 2))
            self.board_contaniner.surface.blit(text, text_rect)
        if field.player is not None and field.player.actual:
            self.border_hexagon(field.x, field.y, field.width, field.height, Colors.WHITE, 5)

    def draw_one_hexagon(self, x, y, width, height, fill_color, border_color):
        self.fill_hexagon(x, y, width, height, fill_color)
        self.border_hexagon(x, y, width, height, border_color)

    def fill_hexagon(self, x, y, width, height, fill_color):
        pygame.draw.polygon(self.board_contaniner.surface, fill_color, [
            (x, y + height // 4),
            (x + width // 2, y),
            (x + width, y + height // 4),
            (x + width, y + 3 * height // 4),
            (x + width // 2, y + height),
            (x, y + 3 * height // 4)
        ])

    def border_hexagon(self, x, y, width, height, border_color, thickness=1):
        pygame.draw.polygon(self.board_contaniner.surface, border_color, [
            (x, y + height // 4),
            (x + width // 2, y),
            (x + width, y + height // 4),
            (x + width, y + 3 * height // 4),
            (x + width // 2, y + height),
            (x, y + 3 * height // 4)
        ], thickness)  # The third argument (1) specifies the line thickness

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

    def draw_container(self, container):
        self.screen.blit(container.surface, (container.x - container.scroll_x, container.y - container.scroll_y))
