from interface import Interface
from grid import Grid

size = (9, 9)
prob = 0.5
grid = Grid(size, prob)
screensize = (800, 800)

game = Interface(grid, screensize)
game.gameloop()

