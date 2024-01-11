import pygame as pg
import os

# colors
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)


class Interface:
    def __init__(self, grid, screensize):
        self.grid = grid  # pass in actual grid later
        self.screensize = screensize
        self.node_size = self.screensize[1] // self.grid.size[1], self.screensize[0] // self.grid.size[0]
        self.loadImages()

    def gameloop(self):
        """Main game loop"""
        pg.init()
        self.screen = pg.display.set_mode(self.screensize)
        pg.display.set_caption('Mine Sweeper')

        status = 'normal'
        while status != 'quit':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    status = 'quit'
                if event.type == pg.MOUSEBUTTONDOWN:
                    click_loc = event.pos  # for buttons
                    if status == 'win':
                        if quit_b.collidepoint(click_loc):
                            status = 'quit'
                        if restart_b.collidepoint(click_loc):
                            status = 'reset'

                    if status == 'lost':
                        if quit_b.collidepoint(click_loc):
                            status = 'quit'
                        if restart_b.collidepoint(click_loc):
                            status = 'reset'
                    x, y = pg.mouse.get_pos()  # using the position to find out which node was clicked
                    row, col = y // self.node_size[0], x // self.node_size[1]  # location
                    current_node = self.grid.node_location(row, col)

                    if status == 'normal':
                        if pg.mouse.get_pressed()[0]:
                            if current_node.flagged:
                                continue
                            current_node.clicked = True  # mark as true to track total number of nodes clicked
                            if current_node.bomb:
                                self.draw('lost')
                                pg.time.wait(300)
                                status = 'lost'
                            self.grid.nodes_clicked += 1
                            self.grid.floodfill(current_node)
                            if self.grid.check_win():
                                status = 'win'

                        if pg.mouse.get_pressed()[2]:  # https://stackoverflow.com/questions/34287938/how-to-distinguish
                            # -left-click-right-click-mouse-clicks-in-pygame
                            current_node.flag()

            if status == 'normal':
                self.draw()

            if status == 'win':
                pg.time.wait(300)
                quit_b = self.create_button(400, 400, 200, 100, 20, 'Quit')

            if status == 'lost':
                self.message('You Suck', 400, 100, 200, 100, 3, 30)
                restart_b = self.create_button(400, 250, 200, 100, 20, 'Restart')
                quit_b = self.create_button(400, 450, 200, 100, 20, 'Quit')

            if status == 'reset':
                self.grid.reset('reset')
                status = 'normal'

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

    def typeimage(self, node, status='normal'):
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

        if status == 'lost':
            if node.bomb:
                if not node.clicked:
                    image = 'unclicked-bomb'
                else:
                    if node.clicked:
                        image = str(node.bomb_count)
                    if not node.bomb:
                        image = 'normal'
                    else:
                        image = 'clicked-bomb'
            if node.flagged:
                if not node.bomb:
                    image = 'wrong-flag'
                else:
                    image = 'flag'

        return self.images[str(image)]

    def draw(self, status='normal'):
        """Draws the board starting from the top left"""
        current = (0, 0)
        for row in range(self.grid.size[0]):
            for col in range(self.grid.size[1]):
                current_node = self.grid.node_location(row, col)
                image = self.typeimage(current_node, status)
                self.screen.blit(image, current)
                current = current[0] + self.node_size[0], current[1]
            current = 0, current[1] + self.node_size[1]

    def create_button(self, x, y, width, height, txt_size, text):
        """Creates button rectangle that is highlighted when cursor hovers over it"""
        # create base button rectangle
        button = pg.Rect(x, y, width, height)

        # position of the mouse
        cursor_pos = pg.mouse.get_pos()
        cursor_hover = button.collidepoint(cursor_pos)

        # makes outline of box gold if cursor is on it
        if cursor_hover:
            pg.draw.rect(self.screen, pg.Color('white'), button)
            pg.draw.rect(self.screen, pg.Color('gold'), button, 3)
        else:
            pg.draw.rect(self.screen, pg.Color('white'), button)
            pg.draw.rect(self.screen, pg.Color('white'), button, 3)

        # adds text to the box after everything else
        font = pg.font.SysFont('squaresans', txt_size)
        text = font.render(f'{text}', True, pg.Color('black'))
        text_rect = text.get_rect(center=button.center)
        self.screen.blit(text, text_rect)
        pg.display.update()
        return button

    def message(self, message, x, y, width, height, border_width, font_size):
        """Displays messages in game by creating objects"""
        # Blit and Load: https: // waylonwalker.com / pygame - image - load /
        # Fonts: https://nerdparadise.com/programming/pygame/part5
        # 10, 350, 480, 140
        square = pg.draw.rect(self.screen, white, (x, y, width, height))
        pg.draw.rect(self.screen, black, (x, y, width, height), border_width)

        font = pg.font.SysFont("squaresans", font_size)
        text = font.render(message, True, black)

        # creates rectangle
        text_rect = text.get_rect(center = square.center)

        # connecting the text with the rectangle as one object
        self.screen.blit(text, text_rect)
