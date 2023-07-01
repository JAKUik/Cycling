from classes.JK_library import *
from view_modules.container import Container


class InfoPanel:
    def __init__(self, x, y, width, height, screen, background):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.background = background
        self.info_panel = Container(self.x, self.y, self.width, self.height, self.screen)
        self.items = {}

    def prepare_info_panel(self):
        # self.info_panel.surface.fill(Colors.YELLOW)
        for item in self.items.values():
            item.draw()
        # self.info_panel.surface.
        pass

    def add_new_item(self, item_id, item):
        self.items[item_id] = item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
