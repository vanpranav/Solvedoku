from scraper import grid
import numpy as np


def check(x, y, val):
    global grid

    for i in range(0, 9):
        if grid[x][i] == val:
            return False

    for i in range(0, 9):
        if grid[i][y] == val:
            return False

    sx = (x // 3) * 3
    sy = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[sx + 0][sy + 0] == val:
                return False
        return True


def solve():
    global grid

    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                for val in range(1, 10):
                    if check(x, y, val):
                        grid[x][y] = val
                        solve()
                        grid[x][y] = 0
                return
    print(np.matrix(grid))
    print()
    input('Next Solution:')
    print()