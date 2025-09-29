import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P2253:
    n_stones = None
    n_unavailable = None
    unavailable = None

    @staticmethod
    def stdin_processor():
        P2253.n_stones, P2253.n_unavailable = map(int, reader().split())
        P2253.unavailable = [False] * (P2253.n_stones + 1)
        for _ in range(P2253.n_unavailable):
            P2253.unavailable[int(reader())] = True
        return

    @staticmethod
    def compute():
        if P2253.unavailable[2]:
            writer("-1\n")
            return
        elif P2253.n_stones == 2:
            writer("1\n")
            return
        """
        1 + 2 + ... + velocity_limit <= n_stones
        velocity_limit * (velocity_limit + 1) <= n_stones * 2 + velocity_limit
        velocity_limit ** 2 <= n_stones * 2
        velocity_limit <= (n_stones * 2) ** 0.5
        """
        velocity_limit = int((2 * P2253.n_stones) ** 0.5) + 1
        visited = [set() for _ in range(P2253.n_stones + 1)]
        velocity_queue = deque()
        velocity_queue.append((2, 1))
        visited[2].add(1)
        step_counter = 0
        while velocity_queue:
            step_counter += 1
            for _ in range(len(velocity_queue)):
                position, v = velocity_queue.popleft()
                if position == P2253.n_stones:
                    writer(f"{step_counter}\n")
                    return
                for next_velocity in (v - 1, v, v + 1):
                    if next_velocity < 1 or next_velocity > velocity_limit:
                        continue
                    next_position = position + next_velocity
                    if next_position > P2253.n_stones or P2253.unavailable[next_position]:
                        continue
                    if next_velocity not in visited[next_position]:
                        visited[next_position].add(next_velocity)
                        velocity_queue.append((next_position, next_velocity))
        writer("-1\n")
        return

    @staticmethod
    def execute():
        P2253.stdin_processor()
        P2253.compute()
        return

P2253.execute()
