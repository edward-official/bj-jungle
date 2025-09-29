import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P11047:
    n_coin_type = None
    coin_type = None
    target_amount = None

    @staticmethod
    def stdin_processor():
        P11047.n_coin_type, P11047.target_amount = map(int, reader().split())
        P11047.coin_type = []
        for _ in range(P11047.n_coin_type):
            P11047.coin_type.append(int(reader().strip()))
        P11047.coin_type.sort(reverse=True)
        return

    @staticmethod
    def compute():
        coin_counter = 0
        for coin_type in P11047.coin_type:
            n = P11047.target_amount // coin_type
            P11047.target_amount -= coin_type * n
            coin_counter += n
            if P11047.target_amount == 0:
                break
        writer(f"{coin_counter}\n")
        return

    @staticmethod
    def execute():
        P11047.stdin_processor()
        P11047.compute()
        return

P11047.execute()