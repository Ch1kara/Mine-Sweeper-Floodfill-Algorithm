from node import Node
import random
class Grid():
    def __init__(self, size, prob):
        self.size = size
        self.board = []
        for row in range(size[0]):
            row = []
            for col in range(size[1]):
                if random.random() < prob:
                    bomb = True
                else:
                    bomb = False
                node = Node(bomb)
                row.append(node)
            self.board.append(row)

    # def neighbors(self, neighbors):
    #     for row in range(row-1,row+1)


