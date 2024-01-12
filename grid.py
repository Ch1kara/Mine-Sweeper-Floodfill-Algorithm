from node import Node
import random


class Grid:
    def __init__(self, size, prob):
        self.prob = prob
        self.size = size
        self.non_bombs = 0
        self.nodes_clicked = 0
        self.grid = []
        for row in range(size[0]):  # list of lists with each node having either a bomb or no bomb
            row = []
            for col in range(size[1]):
                if random.random() < prob:
                    bomb = True
                else:
                    bomb = False
                    self.non_bombs += 1
                node = Node(bomb)
                row.append(node)
            self.grid.append(row)
        self.create_neighbors()

    def node_location(self, row, col):
        """Returns the node given the row and column within the grid"""
        return self.grid[row][col]

    def create_neighbors(self):
        """Adds the neighbors of a given node to the initialized neighbor variable as well as if they have bombs"""
        rows = self.size[0]
        cols = self.size[1]
        for i in range(rows):
            for j in range(cols):
                current_node = self.grid[i][j]
                neighbors = []
                for k in range(i - 1, i + 2):
                    for h in range(j - 1, j + 2):
                        if k == i and h == j:
                            continue
                        if k < 0 or h < 0 or k >= self.size[0] or h >= self.size[1]:
                            continue
                        neighbors.append(self.grid[k][h])
                current_node.set_neighbors_and_bombs(neighbors)

    def check_win(self):
        """Determines if player has won if the number of non-bomb nodes is equal to the nodes clicked"""
        return self.non_bombs == self.nodes_clicked

    def floodfill(self, node):  # https://github.com/vosketalor/minesweeper/blob/main/grid.py
        # https: // vaibhavsethia07.medium.com/flood-fill-algorithm-1424de9863da
        """Implemenation of the floodfill algorithm to recursively click on all non-bomb squares nearby"""
        if node.bomb_count != 0:  # base case
            return
        for neighbor in node.neighbors:
            if not neighbor.clicked and not neighbor.bomb:  # revealed already if clicked and leave alone
                # if neighbor has bomb
                neighbor.clicked = True
                self.nodes_clicked += 1
                self.floodfill(neighbor)  # recursively call floodfill to click all neighboring non-bomb nodes

    def reset(self):
        self.non_bombs = 0
        self.grid = []
        for row in range(self.size[0]):  # list of lists with each node having either a bomb or no bomb
            row = []
            for col in range(self.size[1]):
                if random.random() < self.prob:
                    bomb = True
                else:
                    bomb = False
                    self.non_bombs += 1
                node = Node(bomb)
                node.reset('reset')  # resets the node completely and wipes all info
                row.append(node)
            self.grid.append(row)
        self.create_neighbors()

    def difficulty(self, level):
        if level == 'easy':
            return  Grid((9,9), 0.1)
        if level == 'medium':
            return Grid((16, 16), 0.15)
        if level == 'hard':
            return Grid((20, 20), 0.2)
