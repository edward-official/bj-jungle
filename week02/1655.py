import sys, heapq
reader = sys.stdin.readline
writer = sys.stdout.write

class P1655:
    team_small = []
    team_big = []

    @staticmethod
    def process_input(input):
        if len(P1655.team_small) == len(P1655.team_big):
            heapq.heappush(P1655.team_small, -input)
        else:
            heapq.heappush(P1655.team_big, input)
        if P1655.team_big and P1655.team_small[0] * (-1) > P1655.team_big[0]:
            item1 = heapq.heappop(P1655.team_small) * (-1)
            item2 = heapq.heappop(P1655.team_big) * (-1)
            heapq.heappush(P1655.team_small, item2)
            heapq.heappush(P1655.team_big, item1)
        writer(f"{-P1655.team_small[0]}\n")
        return

    @staticmethod
    def execute():
        n_inputs = int(reader().rstrip())
        for _ in range(n_inputs):
            input = int(reader().rstrip())
            P1655.process_input(input)
        return

P1655.execute()