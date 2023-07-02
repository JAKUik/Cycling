"""
import math
import pygame

class Hexagon:
    def __init__(self, center, size, color, line_width=1, background_color=None):
        self.center = center
        self.size = size
        self.color = color
        self.line_width = line_width
        self.background_color = background_color

    def draw(self, surface):
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            x = self.center[0] + self.size * math.cos(angle)
            y = self.center[1] + self.size * math.sin(angle)
            points.append((x, y))
        if self.background_color:
            pygame.draw.polygon(surface, self.background_color, points)
        pygame.draw.polygon(surface, self.color, points, self.line_width)

# Example usage
pygame.init()
screen = pygame.display.set_mode((400, 300))
hexagon = Hexagon((200, 150), 50, (255, 0, 0), 3, (0, 255, 0))
hexagon.draw(screen)
pygame.display.flip()

"""
import math
import pygame

class Hexagon:
    def __init__(self, center, size, color, background_color=None, line_width=1):
        self.center = center
        self.size = size
        self.color = color
        self.line_width = line_width
        self.background_color = background_color

    def draw(self, surface):
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            x = self.center[0] + self.size * math.cos(angle)
            y = self.center[1] + self.size * math.sin(angle)
            points.append((x, y))
        if self.background_color:
            pygame.draw.polygon(surface, self.background_color, points)
        pygame.draw.polygon(surface, self.color, points, self.line_width)

def axial_to_pixel(q, r, size):
    x = size * 3/2 * q
    y = size * math.sqrt(3) * (r + q/2)
    return x, y

pygame.init()
screen = pygame.display.set_mode((400, 300))

track_tiles = [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1,-1)]
tile_size = 50

i = 20
for q, r in track_tiles:
    x, y = axial_to_pixel(q, r, tile_size)
    hexagon = Hexagon((x + 200, y + 150), tile_size, (255, 255, 255), (255, i, i))
    hexagon.draw(screen)
    i += 30

pygame.display.flip()

while True:
    pass
