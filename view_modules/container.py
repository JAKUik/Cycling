class Container:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        import pygame
        self.surface = pygame.Surface((width, height))
        self.scroll_x = 0
        self.scroll_y = 0
        self.screen = screen

    # def draw(self, screen):
    #     screen.blit(self.surface, (self.x - self.scroll_x, self.y - self.scroll_y))
    #
    def scroll(self, dx, dy):
        self.scroll_x += dx
        if dy > 0:
            self.scroll_y = min(0, self.scroll_y + dy)
        else:
            self.scroll_y = max(self.scroll_y + dy, -self.height + self.screen.get_height() - 10)

    def set_position(self, x=None, y=None):
        """
        :param x: None = no change
        :param y: None = no change
        """
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
