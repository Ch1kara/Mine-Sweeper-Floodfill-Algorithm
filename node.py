class Node():
    def __init__(self, bomb):
        self.clicked = False
        self.flagged = False
        self.bomb = bomb
        self.neighbors = []
        self.bomb_count = 0

    def set_neighbors_and_bombs(self, neighbors):
        """Connects a list of neighbors with a given node and counts the surrounding bombs"""
        self.neighbors = neighbors
        for neighbor in self.neighbors:
            if neighbor.bomb:
                self.bomb_count += 1

    def flag(self):
        """toggles the flag when called upon"""
        if self.flagged:
            self.flagged = False
        else:
            self.flagged = True

