import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2748:
    target_index = None
    dp = None

    @staticmethod
    def process_input():
        P2748.target_index = int(reader())
        P2748.dp = [None for _ in range(P2748.target_index + 1)]
        P2748.dp[0] = 0
        P2748.dp[1] = 1
        return

    @staticmethod
    def fibonacci(n):
        if P2748.dp[n] is not None:
            return P2748.dp[n]
        answer = P2748.fibonacci(n - 1) + P2748.fibonacci(n - 2)
        P2748.dp[n] = answer
        return answer

    @staticmethod
    def execute():
        P2748.process_input()
        writer(f"{P2748.fibonacci(P2748.target_index)}\n")
        return

P2748.execute()