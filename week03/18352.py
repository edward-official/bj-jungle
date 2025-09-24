import sys
from collections import deque

reader = sys.stdin.readline
writer = sys.stdout.write

class P18352:
    n_city = None
    n_road = None
    target_distance = None
    departing_city = None
    adjacent = None

    @staticmethod
    def process_input():
        P18352.n_city, P18352.n_road, P18352.target_distance, P18352.departing_city = map(int, reader().split())
        P18352.adjacent = {city_index: [] for city_index in range(1, P18352.n_city + 1)}
        for _ in range(P18352.n_road):
            c1, c2 = map(int, reader().split())
            P18352.adjacent[c1].append(c2)
        return

    @staticmethod
    def bfs():
        answer = []
        distance = [0] * (P18352.n_city + 1)
        city_queue = deque([P18352.departing_city])
        visited = [False] * (P18352.n_city + 1)
        visited[P18352.departing_city] = True
        while city_queue:
            current_city = city_queue.popleft()
            for next_city in P18352.adjacent[current_city]:
                if not visited[next_city]:
                    distance[next_city] = distance[current_city] + 1
                    if distance[next_city] == P18352.target_distance:
                        answer.append(next_city)
                    city_queue.append(next_city)
                    visited[next_city] = True
        if not answer:
            writer("-1\n")
            return
        answer.sort()
        answer_converted = "\n".join(map(str, answer))
        writer(f"{answer_converted}\n")
        return

    @staticmethod
    def execute():
        P18352.process_input()
        P18352.bfs()
        return

P18352.execute()