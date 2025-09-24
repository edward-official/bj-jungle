from collections import deque
import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2617:
    n_marble = None
    n_comparison = None
    heavier = None
    lighter = None

    @staticmethod
    def process_input():
        P2617.n_marble, P2617.n_comparison = map(int, reader().split())
        P2617.heavier = {marble_index: [] for marble_index in range(1, P2617.n_marble + 1)}
        P2617.lighter = {marble_index: [] for marble_index in range(1, P2617.n_marble + 1)}
        for _ in range(P2617.n_comparison):
            m1, m2 = map(int, reader().split())
            P2617.heavier[m2].append(m1)
            P2617.lighter[m1].append(m2)
        return

    @staticmethod
    def is_impossible(starting_marble):
        heavier_count = 0
        heavier_queue = deque([starting_marble])
        heavier_visited = [False] * (P2617.n_marble + 1)
        heavier_visited[starting_marble] = True
        while heavier_queue:
            popped_marble = heavier_queue.popleft()
            for option in P2617.heavier[popped_marble]:
                if not heavier_visited[option]:
                    heavier_queue.append(option)
                    heavier_visited[option] = True
                    heavier_count += 1
        if heavier_count > P2617.n_marble // 2:
            return True
        lighter_count = 0
        lighter_queue = deque([starting_marble])
        lighter_visited = [False] * (P2617.n_marble + 1)
        lighter_visited[starting_marble] = True
        while lighter_queue:
            popped_marble = lighter_queue.popleft()
            for option in P2617.lighter[popped_marble]:
                if not lighter_visited[option]:
                    lighter_queue.append(option)
                    lighter_visited[option] = True
                    lighter_count += 1
        if lighter_count > P2617.n_marble // 2:
            return True
        return False

    @staticmethod
    def execute():
        P2617.process_input()
        count = 0
        for marble in range(1, P2617.n_marble + 1):
            if P2617.is_impossible(marble):
                count += 1
        writer(f"{count}\n")
        return

P2617.execute()