from node import Node
import random
class Grid():
    def __init__(self, size, prob):
        self.size = size
        self.grid = []
        for row in range(size[0]):
            row = []
            for col in range(size[1]):
                if random.random() < prob:
                    bomb = True
                else:
                    bomb = False
                node = Node(bomb)
                row.append(node)
            self.grid.append(row)

    def node_location(self, row, col):
        return self.grid[row][col]
    # def neighbors(self, neighbors):
    #     for row in range(row-1,row+1)


