import curses
from itertools import product
from more_itertools import repeatfunc

# Doing it in place since they asked even though that's gross
def gameOfLife(board):

    basis = ((-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1), (-1, 1))

    def neighbors(x, y):
        return tuple((x + u, y + v) for u, v in basis)

    h, w = len(board), len(board[0])
    ASLEEP, AWAKE, SLEEP, WAKE = 0, 1, 2, 4

    def status(x, y):
        S = sum(
            board[u][v] & AWAKE for u, v in neighbors(x, y) if 0 <= u < h and 0 <= v < w
        )
        if S < 2 or S > 3:
            return SLEEP
        elif S == 3:
            return WAKE
        else:
            return 0

    def update(cell):
        if cell & SLEEP:
            return ASLEEP
        elif cell & WAKE:
            return AWAKE
        else:
            return cell

    cells = tuple(product(range(h), range(w)))
    for x, y in cells:
        board[x][y] |= status(x, y)
    for x, y in cells:
        board[x][y] = update(board[x][y])
# Runtime: 35 ms, faster than 87.12% of Python3 online submissions for Game of Life.
# Memory Usage: 14.1 MB, less than 12.69% of Python3 online submissions for Game of Life.



def main(scr):
    H, W = scr.getmaxyx()
    curses.curs_set(0)
    curses.use_default_colors()
    INPUT_TIMEOUT_MS = 100
    scr.timeout(INPUT_TIMEOUT_MS)

    board = [[0 for _ in range(20)] for _ in range(20)]
    board[1][1] = 1
    board[1][2] = 1
    board[1][3] = 1
    board[1][4] = 1
    board[2][3] = 1
    board[2][4] = 1
    board[4][3] = 1
    h, w = len(board), len(board[0])
    cells = tuple(product(range(h), range(w)))

    for _ in range(1000):
        scr.clear()
        for x, y in cells:
            display = "*" if board[x][y] else " "
            scr.addstr(x, y, display)
        scr.getch()
        gameOfLife(board)


core = curses.wrapper(main)
