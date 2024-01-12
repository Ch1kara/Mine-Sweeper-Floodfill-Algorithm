from interface import Interface
from grid import Grid

size = (9, 9)
bombprob = 0.1
grid = Grid(size, bombprob)
screensize = (900, 900)

game = Interface(grid, screensize)
game.gameloop()

# Notes for tomorrow:
# - create a home menu before starting game with size control and exit features
#  easy: 9x9, medium: 16x16, hard: 20x20
#  stop click registering after generating from menu screen