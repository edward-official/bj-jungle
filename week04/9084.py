import sys
reader = sys.stdin.readline
write = sys.stdout.write

class P9084:
    @staticmethod
    def testcase():
        n_coin_type = int(reader())
        coin_type = list(map(int, reader().split()))
        coin_type.sort()
        target_amount = int(reader())
        dp = [0] * (target_amount + 1)
        dp[0] = 1
        for coin in coin_type:
            for amount in range(coin, target_amount + 1):
                dp[amount] += dp[amount - coin]
        write(f"{dp[target_amount]}\n")
        return

    @staticmethod
    def execute():
        n_testcase = int(reader())
        for _ in range(n_testcase):
            P9084.testcase()
        return

P9084.execute()