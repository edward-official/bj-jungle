import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P2573:
    n_row = None
    n_column = None
    board = None
    t_board = None
    remaining_point = []

    @staticmethod
    def handle_input():
        P2573.n_row, P2573.n_column = map(int, reader().split())
        P2573.board = [list(map(int, reader().split())) for _ in range(P2573.n_row)]
        P2573.update_remaining()
        return

    @staticmethod
    def update_remaining():
        P2573.remaining_point.clear()
        for row in range(P2573.n_row):
            for column in range(P2573.n_column):
                if P2573.board[row][column] > 0:
                    P2573.remaining_point.append((row, column))
        return

    @staticmethod
    def progress():
        P2573.t_board = [[0 for _ in range(P2573.n_column)] for _ in range(P2573.n_row)]
        for row in range(P2573.n_row):
            for column in range(P2573.n_column):
                if P2573.board[row][column] == 0:
                    continue
                decreasing_amount = 0
                if row - 1 >= 0 and P2573.board[row - 1][column] == 0:
                    decreasing_amount += 1
                if column - 1 >= 0 and P2573.board[row][column - 1] == 0:
                    decreasing_amount += 1
                if row + 1 < P2573.n_row and P2573.board[row + 1][column] == 0:
                    decreasing_amount += 1
                if column + 1 < P2573.n_column and P2573.board[row][column + 1] == 0:
                    decreasing_amount += 1
                t = P2573.board[row][column] - decreasing_amount
                P2573.t_board[row][column] = t if t > 0 else 0
        P2573.board = P2573.t_board
        P2573.update_remaining()
        return

    @staticmethod
    def is_divided():
        if not P2573.remaining_point:
            return False
        remain = set(P2573.remaining_point)
        point_queue = deque()
        start = P2573.remaining_point[0]
        point_queue.append(start)
        remain.remove(start)
        while point_queue:
            r, c = point_queue.popleft()
            if r + 1 < P2573.n_row and (r + 1, c) in remain:
                remain.remove((r + 1, c))
                point_queue.append((r + 1, c))
            if c + 1 < P2573.n_column and (r, c + 1) in remain:
                remain.remove((r, c + 1))
                point_queue.append((r, c + 1))
            if r - 1 >= 0 and (r - 1, c) in remain:
                remain.remove((r - 1, c))
                point_queue.append((r - 1, c))
            if c - 1 >= 0 and (r, c - 1) in remain:
                remain.remove((r, c - 1))
                point_queue.append((r, c - 1))
        return len(remain) > 0

    @staticmethod
    def execute():
        P2573.handle_input()
        counter = 0
        while True:
            if P2573.is_divided():
                break
            P2573.progress()
            counter += 1
            if not P2573.remaining_point:
                counter = 0
                break
        writer(f"{counter}\n")
        return

P2573.execute()
