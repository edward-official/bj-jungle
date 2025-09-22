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
    def update_remaining():
        for row in P2573.n_row:
            for col in P2573.n_column:
                if P2573.board[row][col] > 0:
                    P2573.remaining_point.append((row, col))
        return

    @staticmethod
    def handle_input():
        P2573.n_row, P2573.n_column = map(int, reader().split())
        P2573.board = [list(map(int, input().split())) for _ in range(P2573.n_row)]
        P2573.update_remaining()
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
                if row + 1 <= P2573.n_row - 1 and P2573.board[row + 1][column] == 0:
                    decreasing_amount += 1
                if column + 1 <= P2573.n_column - 1 and P2573.board[row][column + 1] == 0:
                    decreasing_amount += 1
                t = P2573.board[row][column] - decreasing_amount
                P2573.t_board[row][column] = t if t > 0 else 0
        for row in range(P2573.n_row):
            for column in range(P2573.n_column):
                P2573.board[row][column] = P2573.t_board[row][column]
        return

    @staticmethod
    def estimate():
        point_queue = deque([P2573.remaining_point[0]])
        visited = [[False for _ in range(P2573.n_column)] for _ in range(P2573.n_row)]
        visited[point_queue[0][0]][point_queue[0][1]] = True
        P2573.remaining_point.remove(point_queue[0])
        while point_queue:
            popped_point = point_queue.popleft()

        return

    @staticmethod
    def stdout_board():
        for row in range(P2573.n_row):
            writer(f"{P2573.board[row]}\n")
        return

    @staticmethod
    def execute():
        P2573.handle_input()
        P2573.progress()
        P2573.stdout_board()
        return

P2573.execute()