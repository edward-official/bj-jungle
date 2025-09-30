import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P7569:
    R = None
    C = None
    H = None
    tomato3d = None
    remaining_unripe = None
    days_required = None

    @staticmethod
    def stdout_tomato3d():
        for h in range(P7569.H):
            writer("\n")
            for r in range(P7569.R):
                for c in range(P7569.C):
                    writer(f" {P7569.tomato3d[h][r][c]}")
                writer("\n")
        return

    @staticmethod
    def stdin_processor():
        P7569.C, P7569.R, P7569.H = map(int, reader().split())
        P7569.tomato3d = [[[None for _ in range(P7569.C)] for _ in range(P7569.R)] for _ in range(P7569.H)]
        P7569.remaining_unripe = deque()
        for h in range(P7569.H):
            for r in range(P7569.R):
                P7569.tomato3d[h][r] = list(map(int, reader().split()))
                for c in range(P7569.C):
                    if P7569.tomato3d[h][r][c] == 0:
                        P7569.remaining_unripe.append((h, r, c))
        # P7569.stdout_tomato3d()
        return

    @staticmethod
    def point_valid(h, r, c):
        if 0 <= h < P7569.H and 0 <= r < P7569.R and 0 <= c < P7569.C:
            return True
        return False

    @staticmethod
    def is_ripe(h, r, c):
        if P7569.tomato3d[h][r][c] == 1:
            return True
        return False

    @staticmethod
    def proceed_one_day():
        directions = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]
        future_ripe = []
        for unripe in P7569.remaining_unripe:
            h, r, c = unripe
            for d in directions:
                n_h = h + d[0]
                n_r = r + d[1]
                n_c = c + d[2]
                if P7569.point_valid(n_h, n_r, n_c) and P7569.is_ripe(n_h, n_r, n_c):
                    future_ripe.append(unripe)
                    break
        if not future_ripe:
            return False
        for h, r, c in future_ripe:
            P7569.remaining_unripe.remove((h, r, c))
            P7569.tomato3d[h][r][c] = 1
        return True

    @staticmethod
    def compute_days_required():
        P7569.days_required = 0
        while P7569.remaining_unripe:
            if P7569.proceed_one_day():
                P7569.days_required += 1
                if not P7569.remaining_unripe:
                    return
            else:
                P7569.days_required = -1
                return
        return

    @staticmethod
    def stdout_answer():
        writer(f"{P7569.days_required}\n")
        return

    @staticmethod
    def execute():
        P7569.stdin_processor()
        P7569.compute_days_required()
        P7569.stdout_answer()
        return

P7569.execute()