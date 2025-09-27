import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P12865:
    n_item = None
    weight_limit = None
    item = []

    @staticmethod
    def process_input():
        P12865.n_item, P12865.weight_limit = map(int, input().split())
        for _ in range(P12865.n_item):
            w, v = map(int, input().split())
            P12865.item.append((w, v))
        return

    @staticmethod
    def knapsack():
        dp = [0] * (P12865.weight_limit + 1)
        for item_index in range(P12865.n_item):
            w, v = P12865.item[item_index]
            for weight in range(P12865.weight_limit, w - 1, -1):
                dp[weight] = max(dp[weight], dp[weight - w] + v)
        writer(f"{dp[P12865.weight_limit]}\n")
        return

    @staticmethod
    def execute():
        P12865.process_input()
        P12865.knapsack()
        return

P12865.execute()