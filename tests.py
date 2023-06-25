import pygame


class Container:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))
        self.scroll_x = 0
        self.scroll_y = 0

    def draw(self, screen):
        screen.blit(self.surface, (self.x - self.scroll_x, self.y - self.scroll_y))

    def scroll(self, dx, dy):
        self.scroll_x += dx
        self.scroll_y += dy


class ScrollBar:
    def __init__(self, x, y, width, height, orientation='horizontal'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.orientation = orientation
        self.handle_position = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, self.width, self.height))
        if self.orientation == 'horizontal':
            handle_x = self.x + self.handle_position
            handle_y = self.y
            handle_width = 20
            handle_height = self.height
        else:
            handle_x = self.x
            handle_y = self.y + self.handle_position
            handle_width = self.width
            handle_height = 20
        pygame.draw.rect(screen, (100, 100, 100), (handle_x, handle_y, handle_width, handle_height))

    def move_handle(self, dx):
        if self.orientation == 'horizontal':
            max_position = self.width - 20
        else:
            max_position = self.height - 20
        new_position = max(0, min(max_position, self.handle_position + dx))
        delta_position = new_position - self.handle_position
        self.handle_position = new_position
        return delta_position


def main():
    pygame.init()
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    container_width = 300
    container_height = 200

    container_x = (screen_width - container_width) // 2
    container_y = (screen_height - container_height) // 2

    container_surface_width = 500
    container_surface_height = 400

    container_surface_scroll_speed = 5

    container = Container(container_x,
                          container_y,
                          container_width,
                          container_height)
    container.surface.fill((255, 255, 255))
    for i in range(0, container_surface_width, 20):
        pygame.draw.line(container.surface, (0, 0, 0), (i, 0), (i, container_surface_height))
    for i in range(0, container_surface_height, 20):
        pygame.draw.line(container.surface, (0, 0, 0), (0, i), (container_surface_width, i))

    h_scrollbar = ScrollBar(container_x,
                            container_y + container_height,
                            container_width,
                            20)
    v_scrollbar = ScrollBar(container_x + container_width,
                            container_y,
                            20,
                            container_height)

    running = True

    # ...
    # (zbytek kódu z předchozí odpovědi)
    # ...

    running = True
    dragging_h_scrollbar = False
    dragging_v_scrollbar = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = h_scrollbar.move_handle(-10)
                    container.scroll(dx * container_surface_scroll_speed, 0)
                elif event.key == pygame.K_RIGHT:
                    dx = h_scrollbar.move_handle(10)
                    container.scroll(dx * container_surface_scroll_speed, 0)
                elif event.key == pygame.K_UP:
                    dy = v_scrollbar.move_handle(-10)
                    container.scroll(0, -dy * container_surface_scroll_speed)
                elif event.key == pygame.K_DOWN:
                    dy = v_scrollbar.move_handle(10)
                    container.scroll(0, -dy * container_surface_scroll_speed)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if h_scrollbar.x <= mouse_x <= h_scrollbar.x + h_scrollbar.width and h_scrollbar.y <= mouse_y <= h_scrollbar.y + h_scrollbar.height:
                    dragging_h_scrollbar = True
                elif v_scrollbar.x <= mouse_x <= v_scrollbar.x + v_scrollbar.width and v_scrollbar.y <= mouse_y <= v_scrollbar.y + v_scrollbar.height:
                    dragging_v_scrollbar = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_h_scrollbar = False
                dragging_v_scrollbar = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging_h_scrollbar:
                    dx = event.rel[0]
                    dx = h_scrollbar.move_handle(dx)
                    container.scroll(dx * container_surface_scroll_speed, 0)
                elif dragging_v_scrollbar:
                    dy = event.rel[1]
                    dy = v_scrollbar.move_handle(dy)
                    container.scroll(0, -dy * container_surface_scroll_speed)

        screen.fill((200, 200, 200))
        container.draw(screen)
        h_scrollbar.draw(screen)
        v_scrollbar.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()



#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     dx = h_scrollbar.move_handle(-10)
#                     container.scroll(-dx * container_surface_scroll_speed, 0)
#                 elif event.key == pygame.K_RIGHT:
#                     dx = h_scrollbar.move_handle(10)
#                     container.scroll(-dx * container_surface_scroll_speed, 0)
#                 elif event.key == pygame.K_UP:
#                     dy = v_scrollbar.move_handle(-10)
#                     container.scroll(0, -dy * container_surface_scroll_speed)
#                 elif event.key == pygame.K_DOWN:
#                     dy = v_scrollbar.move_handle(10)
#                     container.scroll(0, -dy * container_surface_scroll_speed)
#
#         screen.fill((200, 200, 200))
#         container.draw(screen)
#         h_scrollbar.draw(screen)
#         v_scrollbar.draw(screen)
#         pygame.display.flip()
#         clock.tick(60)
#
# if __name__ == '__main__':
#     main()
