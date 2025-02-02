from random import randint, choice, gauss

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# random color function
def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))
