import sys
from copy import deepcopy
reader = sys.stdin.readline
writer = sys.stdout.write

class P7569:
    R = None
    C = None
    H = None
    tomato3d = None
    opening = None
    days_required = None

    @staticmethod
    def stdin_processor():
        P7569.C, P7569.R, P7569.H = map(int, reader().split())
        P7569.tomato3d = [[[None for _ in range(P7569.C)] for _ in range(P7569.R)] for _ in range(P7569.H)]
        P7569.opening = []
        for h in range(P7569.H):
            for r in range(P7569.R):
                P7569.tomato3d[h][r] = list(map(int, reader().split()))
                for c in range(P7569.C):
                    if P7569.tomato3d[h][r][c] == 1:
                        P7569.opening.append((h, r, c))
        return

    @staticmethod
    def is_point_in_range(h, r, c):
        if 0 <= h < P7569.H and 0 <= r < P7569.R and 0 <= c < P7569.C:
            return True
        return False

    @staticmethod
    def is_unripe_left():
        for h in range(P7569.H):
            for r in range(P7569.R):
                for c in range(P7569.C):
                    if P7569.tomato3d[h][r][c] == 0:
                        return True
        return False

    @staticmethod
    def bfs():
        direction = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]
        visited = set(P7569.opening)
        point_stack = P7569.opening
        P7569.days_required = 0
        changes = []
        if not point_stack:
            P7569.days_required = -1
            return
        while point_stack:
            popped = point_stack.pop()
            h, r, c = popped
            for d in direction:
                n_h = h + d[0]
                n_r = r + d[1]
                n_c = c + d[2]
                if P7569.is_point_in_range(n_h, n_r, n_c):
                    if P7569.tomato3d[n_h][n_r][n_c] == 0 and (n_h, n_r, n_c) not in visited:
                        changes.append((n_h, n_r, n_c))
                        visited.add((n_h, n_r, n_c))
            if not point_stack:
                # P7569.stdout_tomato3d()
                if not changes:
                    if P7569.is_unripe_left():
                       P7569.days_required = -1
                    return
                else:
                    P7569.days_required += 1
                    point_stack.clear()
                    for t in changes:
                        point_stack.append(t)
                    for h, r, c in changes:
                        P7569.tomato3d[h][r][c] = 1
                    changes.clear()
        return

    @staticmethod
    def stdout_tomato3d():
        writer("----------------------------------")
        for h in range(P7569.H):
            writer("\n")
            for r in range(P7569.R):
                for c in range(P7569.C):
                    writer(f"{P7569.tomato3d[h][r][c]:4d}")
                writer("\n")
        return

    @staticmethod
    def stdout_answer():
        writer(f"{P7569.days_required}\n")
        return

    @staticmethod
    def execute():
        P7569.stdin_processor()
        P7569.bfs()
        P7569.stdout_answer()
        return

P7569.execute()