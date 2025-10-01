import sys, heapq
reader = sys.stdin.readline
writer = sys.stdout.write

class P1432:
    n_points = None
    previous_points = None
    outdegree = None
    answer = None

    @staticmethod
    def stdin_previous_points():
        P1432.n_points = int(reader())
        P1432.previous_points = [[] for _ in range(P1432.n_points + 1)]
        P1432.outdegree = [0] * (P1432.n_points + 1)
        for departing_index in range(1, P1432.n_points + 1):
            t = reader().strip()
            for arriving_index in range(1, P1432.n_points + 1):
                if t[arriving_index-1] == "1":
                    P1432.outdegree[departing_index] += 1
                    P1432.previous_points[arriving_index].append(departing_index)
        return

    @staticmethod
    def compute_answer():
        P1432.answer = [0] * (P1432.n_points + 1)
        point_heap = []
        for departing_index in range(1, P1432.n_points + 1):
            if P1432.outdegree[departing_index] == 0:
                heapq.heappush(point_heap, -departing_index)
        index_modifier = P1432.n_points
        while point_heap:
            destination_index = -heapq.heappop(point_heap)
            P1432.answer[destination_index] = index_modifier
            index_modifier -= 1
            for origin_index in P1432.previous_points[destination_index]:
                P1432.outdegree[origin_index] -= 1
                if P1432.outdegree[origin_index] == 0:
                    heapq.heappush(point_heap, -origin_index)
        if index_modifier != 0:
            writer("-1\n")
        else:
            for index in range(1, P1432.n_points + 1):
                writer(f"{P1432.answer[index]} ")
        return

    @staticmethod
    def execute():
        P1432.stdin_previous_points()
        P1432.compute_answer()
        return

P1432.execute()
