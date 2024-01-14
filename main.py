from interface import Interface
from grid import Grid

size = (9, 9)
bombprob = 0.1
grid = Grid(size, bombprob)
screensize = (900, 900)

game = Interface(grid, screensize)
game.gameloop()