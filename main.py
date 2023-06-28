from classes.mainmenu import MainMenu

import pygame
pygame.init()

# Constants
CLOCK_TICK = 30

if __name__ == '__main__':
    main = MainMenu()
    main.main_menu()
    pass

# board = Board(400, 25)
# output = ViewModule(screen_widht, screen_height, board)

pygame.quit()
