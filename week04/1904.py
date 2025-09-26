import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P1904:
    target_index = None
    dp = None

    @staticmethod
    def process_input():
        P1904.target_index = int(reader())
        P1904.dp = [None] * (P1904.target_index + 1)
        P1904.dp[0] = 1
        P1904.dp[1] = 1
        return

    @staticmethod
    def compute():
        for index in range(2, P1904.target_index + 1):
            P1904.dp[index] = (P1904.dp[index - 1] + P1904.dp[index - 2]) % 15746
        writer(f"{P1904.dp[P1904.target_index]}\n")
        return

    @staticmethod
    def execute():
        P1904.process_input()
        P1904.compute()
        return

P1904.execute()