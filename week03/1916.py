from collections import deque
import sys, math, heapq
reader = sys.stdin.readline
writer = sys.stdout.write

class P1916:
    n_city = None
    n_bus = None
    adjacent = None
    departing_city = None
    arriving_city = None

    @staticmethod
    def process_input():
        P1916.n_city = int(reader())
        P1916.n_bus = int(reader())
        P1916.adjacent = {city_index: [] for city_index in range(1, P1916.n_city + 1)}
        for _ in range(P1916.n_bus):
            city1, city2, distance = map(int, reader().split())
            P1916.adjacent[city1].append((city2, distance))
        P1916.departing_city, P1916.arriving_city = map(int, reader().split())
        return

    @staticmethod
    def dijkstra():
        distance = [math.inf] * (P1916.n_city + 1)
        distance[P1916.departing_city] = 0
        city_pq = [(0, P1916.departing_city)]
        while city_pq:
            current_distance, current_city = heapq.heappop(city_pq)
            # writer(f"\ncurrent city: {current_city} (distance: {current_distance})\n")
            if current_city == P1916.arriving_city:
                writer(f"{current_distance}\n")
                return
            for next_city, next_distance in P1916.adjacent[current_city]:
                # writer(f"distance from current city ({current_city}) to next city ({next_city}): {next_distance}\n")
                candidate_distance = current_distance + next_distance
                if distance[next_city] > candidate_distance:
                    distance[next_city] = candidate_distance
                    heapq.heappush(city_pq, (candidate_distance, next_city))
                # writer(f"distance: {str(distance[1:]):30s} queue: {city_pq}\n")
        return

    @staticmethod
    def execute():
        P1916.process_input()
        P1916.dijkstra()
        return

P1916.execute()