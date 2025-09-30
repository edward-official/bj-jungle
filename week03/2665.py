import heapq
import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2665:
    side = None
    board = None
    distance = None

    @staticmethod
    def stdin_processor():
        P2665.side = int(reader())
        P2665.board = []
        for row in range(P2665.side):
            P2665.board.append(reader().strip())
        return

    @staticmethod
    def range_checker(row, column):
        if 0 <= row < P2665.side and 0 <= column < P2665.side:
            return True
        return False

    @staticmethod
    def stdout_distance():
        writer("\n")
        for row in range(P2665.side):
            writer(f"{P2665.distance[row]}\n")
        return

    @staticmethod
    def dijksta():
        P2665.distance = [[10 ** 3 for _ in range(P2665.side)] for _ in range(P2665.side)]
        P2665.distance[0][0] = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        point_pq = [(0,0,0)]
        while point_pq:
            distance, row, column = heapq.heappop(point_pq)
            for d in directions:
                n_row, n_column = row + d[0], column + d[1]
                if P2665.range_checker(n_row, n_column):
                    n_distance = distance + (1 if P2665.board[n_row][n_column] == "0" else 0)
                    if n_distance < P2665.distance[n_row][n_column]:
                        P2665.distance[n_row][n_column] = n_distance
                        heapq.heappush(point_pq, (n_distance, n_row, n_column))
        return

    @staticmethod
    def stdout_processor():
        writer(f"{P2665.distance[P2665.side-1][P2665.side-1]}\n")
        return

    @staticmethod
    def execute():
        P2665.stdin_processor()
        P2665.dijksta()
        P2665.stdout_processor()
        return

P2665.execute()