import pygame


class Drawable:
    def __init__(self, surface, position):
        self.position = position
        self.surface = surface

    def draw(self):
        pass


class DrawText(Drawable):
    def __init__(self, surface, position, text, font, color):
        super().__init__(surface, position)
        self.text = text
        self.font = pygame.font.Font(None, font)
        self.color = color

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        self.surface.surface.blit(text_surface, self.position)


class DrawList(Drawable):
    def __init__(self, surface, position, multiline_text, font, color):
        super().__init__(surface, position)
        self.text = multiline_text
        self.font = pygame.font.Font(None, font)
        self.color = color

    def draw(self):
        lines = self.text.split('\n')
        y_offset = 0
        for line in lines:
            text_surface = self.font.render(line, True, self.color)
            self.surface.surface.blit(text_surface, (self.position[0], self.position[1] + y_offset))
            y_offset += self.font.get_height() + 5


class DrawImage(Drawable):
    def __init__(self, position, image_path):
        super().__init__(position)
        self.image = pygame.image.load(image_path)

    def draw(self):
        self.surface.blit(self.image, self.position)
