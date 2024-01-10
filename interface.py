import pygame as pg
import os
class Interface():
    def __init__(self, grid, size):
        self.grid = grid # pass in actual grid later
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
            self.draw()
            pg.display.flip()
        pg.quit()

    def loadImages(self):
        """Maps png image to a pygame image object"""
        self.images = {}
        directory = 'images'
        for name in os.listdir(directory):
            path = directory + "/" + name
            image = pg.image.load(path)
            image = pg.transform.scale(image, self.node_size) # https://github.com/google/google-ctf/blob/7dc15ebb26df0
            # c83a3eafd7ebd24410d85edca68/2023/quals/misc-mine-the-gap/src/minesweeper.py#L45
            self.images[name.split(".")[0]] = image

    def draw(self):
        """Draws the board starting from the top left"""
        current = (0, 0)
        for row in range(self.grid.size[0]):
            for col in range(self.grid.size[1]):
                image = self.images['normal']
                self.screen.blit(image, current)
                current = current[0] + self.node_size[0], current[1]
            current = 0, current[1] + self.node_size[1]
