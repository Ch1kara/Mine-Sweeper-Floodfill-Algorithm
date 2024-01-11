from node import Node
import random


class Grid():
    def __init__(self, size, prob):
        self.size = size
        self.grid = []
        for row in range(size[0]):  # list of lists with each node having either a bomb or no bomb
            row = []
            for col in range(size[1]):
                if random.random() < prob:
                    bomb = True
                else:
                    bomb = False
                node = Node(bomb)
                row.append(node)
            self.grid.append(row)
        self.create_neighbors()

    def node_location(self, row, col):
        return self.grid[row][col]

    def create_neighbors(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
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
