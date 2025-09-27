import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P9251:
    @staticmethod
    def execute():
        string1 = reader().rstrip()
        string2 = reader().rstrip()
        dp = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
        for index1 in range(1, len(string1) + 1):
            for index2 in range(1, len(string2) + 1):
                if string1[index1-1] == string2[index2-1]:
                    dp[index1][index2] = dp[index1-1][index2-1] + 1
                else:
                    dp[index1][index2] = max(dp[index1-1][index2], dp[index1][index2-1])
        writer(f"{dp[len(string1)][len(string2)]}\n")
        return

P9251.execute()