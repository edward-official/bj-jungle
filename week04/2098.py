import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2098:
    n_cities = None
    cost_board = None
    ALL_VISITED = None
    INF = 10**15
    dpm = None

    @staticmethod
    def process_input():
        P2098.n_cities = int(reader())
        P2098.cost_board = [list(map(int, reader().split())) for _ in range(P2098.n_cities)]
        P2098.ALL_VISITED = (1 << P2098.n_cities) - 1
        P2098.dpm = [[-1 for _ in range(P2098.n_cities)] for _ in range(1 << P2098.n_cities)]
        return

    @staticmethod
    def compute_cost(visited_mask, current_city):
        if visited_mask == P2098.ALL_VISITED:
            return P2098.cost_board[current_city][0] if P2098.cost_board[current_city][0] != 0 else P2098.INF
        if P2098.dpm[visited_mask][current_city] != -1:
            return P2098.dpm[visited_mask][current_city]
        best = P2098.INF
        for next_city in range(P2098.n_cities):
            if (visited_mask & (1 << next_city)) != 0:
                continue
            move_cost = P2098.cost_board[current_city][next_city]
            if move_cost == 0:
                continue
            candidate = move_cost + P2098.compute_cost(visited_mask | (1 << next_city), next_city)
            if candidate < best:
                best = candidate
        P2098.dpm[visited_mask][current_city] = best
        return best

    @staticmethod
    def execute():
        P2098.process_input()
        visited_mask = 1 << 0
        answer = P2098.compute_cost(visited_mask, 0)
        writer(f"{answer}\n")
        return

P2098.execute()