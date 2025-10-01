import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P3055:
    n_rows = None
    n_columns = None
    forest = None
    flood_queue = None
    route_queue = None
    visited = None
    required_time = None

    @staticmethod
    def stdin_forest():
        P3055.n_rows, P3055.n_columns = map(int, reader().split())
        P3055.forest = [[None for _ in range(P3055.n_columns)] for _ in range(P3055.n_rows)]
        for r in range(P3055.n_rows):
            t = reader().strip()
            for c in range(P3055.n_columns):
                P3055.forest[r][c] = t[c]
        return

    @staticmethod
    def opening_setup():
        P3055.flood_queue = deque()
        P3055.route_queue = deque()
        P3055.visited = set()
        P3055.required_time = [[1 << 20 for _ in range(P3055.n_columns)] for _ in range(P3055.n_rows)]
        for row in range(P3055.n_rows):
            for column in range(P3055.n_columns):
                if P3055.forest[row][column] == "S":
                    P3055.required_time[row][column] = 0
                    P3055.route_queue.append((row, column))
                elif P3055.forest[row][column] == "*":
                    P3055.flood_queue.append((row, column))
        return

    @staticmethod
    def is_point_in_range(r, c):
        if 0<=r<P3055.n_rows and 0<=c<P3055.n_columns:
            return True
        return False

    @staticmethod
    def compute_required_time_to_den():
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while P3055.route_queue:
            for _ in range(len(P3055.flood_queue)):
                r, c = P3055.flood_queue.popleft()
                for d in direction:
                    n_r = r + d[0]
                    n_c = c + d[1]
                    if not P3055.is_point_in_range(n_r, n_c):
                        continue
                    elif P3055.forest[n_r][n_c] == ".":
                        P3055.forest[n_r][n_c] = "*"
                        P3055.flood_queue.append((n_r, n_c))
            for _ in range(len(P3055.route_queue)):
                r, c = P3055.route_queue.popleft()
                for d in direction:
                    n_r = r + d[0]
                    n_c = c + d[1]
                    if not P3055.is_point_in_range(n_r, n_c):
                        continue
                    elif P3055.forest[n_r][n_c] == "." and (n_r, n_c) not in P3055.visited:
                        P3055.route_queue.append((n_r, n_c))
                        P3055.visited.add((n_r, n_c))
                        P3055.required_time[n_r][n_c] = P3055.required_time[r][c] + 1
                    elif P3055.forest[n_r][n_c] == "D":
                        P3055.required_time[n_r][n_c] = P3055.required_time[r][c] + 1
                        writer(f"{P3055.required_time[n_r][n_c]}\n")
                        return
            # P3055.stdout_forest()
            # P3055.stdout_time()
            # writer("\n")
        writer("KAKTUS\n")
        return

    @staticmethod
    def stdout_forest():
        for r in range(P3055.n_rows):
            writer(f"{P3055.forest[r]}\n")
        return

    @staticmethod
    def stdout_time():
        for r in range(P3055.n_rows):
            writer(f"{P3055.required_time[r]}\n")

    @staticmethod
    def execute():
        P3055.stdin_forest()
        P3055.opening_setup()
        P3055.compute_required_time_to_den()
        return

P3055.execute()