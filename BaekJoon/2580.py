#2580
import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

def check():
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
                return False, i, j
    return True, -1, -1

def go(y, x, n):
    for i in range(9):
        if board[i][x] == n or board[y][i] == n:
            return False
        sy = (y // 3) * 3 + i // 3
        sx = (x // 3) * 3 + i % 3
        if board[sy][sx] == n:
            return False
    return True

def print_board():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()

def solve_dfs():
    flag, y, x = check()
    if flag:
        print_board()
        exit(0)
    for i in range(1, 10):
        if go(y, x, i):
            board[y][x] = i
            solve_dfs()
            board[y][x] = 0

solve_dfs()