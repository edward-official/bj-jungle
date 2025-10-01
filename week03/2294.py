import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2294:
    P_INF = 10 ** 6
    n_coin = None
    target_amount = None
    coin = []
    minimum_number_of_coin = []

    @staticmethod
    def stdin_processor():
        P2294.n_coin, P2294.target_amount = map(int, reader().split())
        for _ in range(P2294.n_coin):
            P2294.coin.append(int(reader().strip()))
        return

    @staticmethod
    def opening_setup():
        P2294.minimum_number_of_coin = [P2294.P_INF for _ in range(P2294.target_amount + 1)]
        P2294.minimum_number_of_coin[0] = 0
        P2294.coin = list(set(P2294.coin))
        P2294.coin.sort()
        return

    @staticmethod
    def compute():
        for coin in P2294.coin:
            if P2294.target_amount < coin:
                break
            for amount in range(coin, P2294.target_amount + 1):
                P2294.minimum_number_of_coin[amount] = min(P2294.minimum_number_of_coin[amount], P2294.minimum_number_of_coin[amount - coin] + 1)
            # writer(f"{P2294.minimum_number_of_coin}\n")
        return

    @staticmethod
    def stdout_answer():
        if P2294.minimum_number_of_coin[P2294.target_amount] == P2294.P_INF:
            writer("-1")
            return
        writer(f"{P2294.minimum_number_of_coin[P2294.target_amount]}\n")
        return

    @staticmethod
    def execute():
        P2294.stdin_processor()
        P2294.opening_setup()
        P2294.compute()
        P2294.stdout_answer()
        return

P2294.execute()