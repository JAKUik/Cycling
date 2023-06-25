import pygame
from .JK_library import *
from .container import Container

class GameOutput:
    def __init__(self, window_width, window_height, game_board):
        pygame.init()
        self.window_width = window_width
        self.window_height = window_height
        self.game_board = game_board
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Cycling Game")
        # Set white background
        self.background_color = LIGHT_GRAY
        # self.screen.fill(self.background_color)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 20)
        # Calculate the dimensions of the hexagon
        self.hexagon_width = self.window_width // 35
        # hexagon_height = int(hexagon_width * 0.866)
        self.hexagon_height = int(self.hexagon_width * 1)

        self.board_contaniner = Container(10, 0, self.window_width // 4 * 3, self.hexagon_height
                                          * self.game_board.rows * 0.75 + 10, self.screen)
        self.board_contaniner.surface.fill(DARK_GREEN)

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

    def draw_field(self, field, x, y, width, height):
        """
        Draw one hexagon field
        :param field:
        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """
        bg = field.bg_color
        if field.player is not None:
            bg = field.player.team.color

        pygame.draw.polygon(self.board_contaniner.surface, bg, [
            (x, y + height // 4),
            (x + width // 2, y),
            (x + width, y + height // 4),
            (x + width, y + 3 * height // 4),
            (x + width // 2, y + height),
            (x, y + 3 * height // 4)
        ])

        # Draw the black outline of the hexagon
        pygame.draw.polygon(self.board_contaniner.surface, (0, 0, 0), [
            (x, y + height // 4),
            (x + width // 2, y),
            (x + width, y + height // 4),
            (x + width, y + 3 * height // 4),
            (x + width // 2, y + height),
            (x, y + 3 * height // 4)
        ], 1)  # The third argument (1) specifies the line thickness

        # Render the field's coordinates as text
        if not field.enable:
            # Blit the text onto the surface
            text = self.font.render(f"{field.row},{field.col}", True, BLACK)
            text_rect = text.get_rect(center=(x + width / 2, y + height / 2))
            self.board_contaniner.surface.blit(text, text_rect)
        elif field.player is not None:
            text = self.font.render(f"{field.player.initials}", True, BLACK)
            text_rect = text.get_rect(center=(x + width / 2, y + height / 2))
            self.board_contaniner.surface.blit(text, text_rect)


        # Render Player


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
