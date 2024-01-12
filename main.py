from interface import Interface
from grid import Grid

size = (9, 9)
bombprob = 0.2
grid = Grid(size, bombprob)
screensize = (900, 900)

game = Interface(grid, screensize)
game.gameloop()

# Notes for tomorrow:
# - if won, go to win screen for 5-10 seconds(maybe transparent so you can still see screen)
# - create a home menu before starting game with size control and exit features