class Node():
    def __init__(self, bomb):
        self.clicked = False
        self.flagged = False
        self.bomb = bomb
        self.neighbors = []
