import slau
from function import *
import sys


ROUND_LVL = 4
COLOUMN_SIZE = 12


def print_table_row(row):
    for i in row:
        if type(i) == str:
            print(i.ljust(COLOUMN_SIZE), end=' | ')
        else:
            print(str(round(i, 4)).ljust(COLOUMN_SIZE), end=' | ')
    print()


def print_table_header(row):
    for i in row:
        print(str(i).ljust(COLOUMN_SIZE), end=' | ')
    print("\n" + len(row) * (COLOUMN_SIZE + 3) * "-")


def mid(a, b):
    return (a + b) / 2


def is_dif_sign(a, b):
    return (a > 0 and b < 0) or (a < 0 and b > 0)


def add_vertical_line(x, arr):
    arr[0].append(x)
    arr[1].append(0)
    arr[0].append(x)
    arr[1].append(1)


def solve_slau(matrix, free_v):
    res = slau.gauss_(matrix, free_v)
    return slau.rev_calc(res[0], res[1])


def fill_rev_diag(matrix, value: int, lvl: int):
    x, y = 0, 0
    if lvl < len(matrix):
        x = 0
        y = lvl
    elif len(matrix) <= lvl < (len(matrix) + len(matrix[0])):
        x = lvl - len(matrix) + 1
        y = len(matrix) - 1
    else:
        print("Diagonal fill error, aborting", file=sys.stderr)
        sys.exit(-1)

    while x < len(matrix[0]) and y >= 0:
        matrix[y][x] = value
        x += 1
        y -= 1


def find_R2(f: Function, points):
    mid_f = 0
    for p in points: mid_f += f.calc(p[0])
    mid_f /= len(points)

    S1, S2 = 0, 0
    for p in points:
        S1 += (p[1] - f.calc(p[0])) ** 2
        S2 += (p[1] - mid_f) ** 2
    res = 1 - S1 / S2
    return res if res >= 0 else 0


def check_accuracy(f: Function, points):
    delta, eps, R2 = 0, 0, 0
    for i in range(len(points)):
        _y = f.calc(points[i][0])
        delta += (_y - points[i][1]) ** 2

    eps = m.sqrt(delta / len(points))
    R2 = find_R2(f, points)
    return delta, eps, R2
