from interface import Interface
from grid import Grid

size = (20, 20)
bombprob = 0.1
grid = Grid(size, bombprob)
screensize = (1000, 1000)

game = Interface(grid, screensize)
game.gameloop()

# Notes for tomorrow:
# - if lost, don't allow any more clicking and reveal all remaining bombs(maybe with some animations/time in between
# if incorrect flags, use wrong-flag.png. If unclicked bomb, blow it up
# - if won, go to win screen for 5-10 seconds(maybe transparent so you can still see screen)
# - create a play again button/menu after the win loss states
# - create a home menu before starting game with size control and exit features