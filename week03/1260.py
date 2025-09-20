import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
reader = sys.stdin.readline
writer = sys.stdout.write


class P1260:
    n_node = None
    n_edge = None
    departing_point = None
    adjacent = {}
    visited = None
    answer = []

    @staticmethod
    def process_input():
        P1260.n_node, P1260.n_edge, P1260.departing_point = map(int, reader().split())
        P1260.adjacent = {node_index: [] for node_index in range(1, P1260.n_node + 1)}
        for _ in range(P1260.n_edge):
            node1, node2 = map(int, reader().split())
            P1260.adjacent[node1].append(node2)
            P1260.adjacent[node2].append(node1)
        for node_index in range(1, P1260.n_node + 1):
            P1260.adjacent[node_index].sort()
        return

    @staticmethod
    def _dfs(current_node):
        P1260.visited[current_node] = True
        P1260.answer.append(current_node)
        for connected_node in P1260.adjacent[current_node]:
            if not P1260.visited[connected_node]:
                P1260._dfs(connected_node)
        return

    @staticmethod
    def dfs():
        P1260.visited = [False] * (P1260.n_node + 1)
        P1260.answer.clear()
        P1260._dfs(P1260.departing_point)
        writer(f"{' '.join(map(str, P1260.answer))}\n")
        return

    @staticmethod
    def bfs():
        P1260.visited = [False] * (P1260.n_node + 1)
        P1260.visited[P1260.departing_point] = True
        P1260.answer.clear()
        queue_node = deque()
        queue_node.append(P1260.departing_point)
        while queue_node:
            current_node = queue_node.popleft()
            P1260.visited[current_node] = True
            P1260.answer.append(current_node)
            for connected_node in P1260.adjacent[current_node]:
                if not P1260.visited[connected_node] and connected_node not in queue_node:
                    queue_node.append(connected_node)
        writer(f"{' '.join(map(str, P1260.answer))}\n")

    @staticmethod
    def execute():
        P1260.process_input()
        P1260.dfs()
        P1260.bfs()
        return


P1260.execute()
