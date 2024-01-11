import pygame as pg
import os
from grid import Grid
from node import Node


class Interface():
    def __init__(self, grid, size):
        self.grid = grid  # pass in actual grid later
        self.size = size
        self.node_size = self.size[1] // self.grid.size[1], self.size[0] // self.grid.size[0]
        self.loadImages()

    def gameloop(self):
        """Main game loop"""
        pg.init()
        self.screen = pg.display.set_mode(self.size)
        pg.display.set_caption('Mine Sweeper')

        status = 'normal'
        while status != 'quit':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    status = 'quit'
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[0]:
                        x, y = pg.mouse.get_pos()  # using the position to find out which node was clicked
                        row, col = y // self.node_size[0], x // self.node_size[1]
                        current_node = self.grid.node_location(row, col)
                        current_node.clicked = True  # mark as true to track total number of nodes clicked
                        if current_node.flagged:  # left click won't do anything to a flagged node
                            continue
                        if current_node.bomb:
                            self.grid.lost = True  # maybe works, maybe doesn't
                        self.grid.nodes_clicked += 1
                        self.grid.check_win()
                        self.grid.floodfill(current_node)

                    if pg.mouse.get_pressed()[2]:  # https://stackoverflow.com/questions/34287938/how-to-distinguish
                        # -left-click-right-click-mouse-clicks-in-pygame
                        x, y = pg.mouse.get_pos()  # using the position to find out which node was clicked
                        row, col = y // self.node_size[0], x // self.node_size[1]
                        current_node = self.grid.node_location(row, col)
                        current_node.flag()
            self.draw()
            pg.display.flip()
        pg.quit()

    def loadImages(self):
        """Maps png image to a pygame image object"""
        self.images = {}  # dictionary with key as string before .png and value as the image object
        directory = 'images'
        for name in os.listdir(directory):
            path = directory + "/" + name
            image = pg.image.load(path)
            image = pg.transform.scale(image, self.node_size)  # https://github.com/google/google-ctf/blob/7dc15ebb26df0
            # c83a3eafd7ebd24410d85edca68/2023/quals/misc-mine-the-gap/src/minesweeper.py#L45
            self.images[name.split(".")[0]] = image

    def typeimage(self, node):
        """Determines the type of node """
        if node.clicked:
            if node.bomb:
                image = 'clicked-bomb'
            else:
                image = str(node.bomb_count)
        else:
            if node.flagged:
                image = 'flag'
            else:
                image = 'normal'
        return self.images[str(image)]

    def draw(self):
        """Draws the board starting from the top left"""
        current = (0, 0)
        for row in range(self.grid.size[0]):
            for col in range(self.grid.size[1]):
                current_node = self.grid.node_location(row, col)
                image = self.typeimage(current_node)
                self.screen.blit(image, current)
                current = current[0] + self.node_size[0], current[1]
            current = 0, current[1] + self.node_size[1]
