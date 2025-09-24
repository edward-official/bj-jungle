import sys
from collections import deque

reader = sys.stdin.readline
writer = sys.stdout.write

class P2178:
    n_row = None
    n_column = None
    board = None

    @staticmethod
    def process_input():
        P2178.n_row, P2178.n_column = map(int, reader().split())
        P2178.board = [[int(letter) for letter in reader().rstrip()] for _ in range(P2178.n_row)]
        return

    @staticmethod
    def bfs():
        distance = [[0 for _ in range(P2178.n_column)] for _ in range(P2178.n_row)]
        visited = [[False for _ in range(P2178.n_column)] for _ in range(P2178.n_row)]
        point_queue = deque([(0, 0)])
        visited[0][0] = True
        while point_queue:
            r, c = point_queue.popleft()
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in direction:
                nr = r + dr
                nc = c + dc
                if (0 <= nr <= P2178.n_row - 1) and (0 <= nc <= P2178.n_column - 1) and (not visited[nr][nc]) and (P2178.board[nr][nc]) == 1:
                    distance[nr][nc] = distance[r][c] + 1
                    if nr == P2178.n_row - 1 and nc == P2178.n_column - 1:
                        writer(f"{distance[nr][nc] + 1}\n")
                        return
                    point_queue.append((nr, nc))
                    visited[nr][nc] = True
        return

    @staticmethod
    def execute():
        P2178.process_input()
        P2178.bfs()
        return

P2178.execute()