import sys
from collections import deque

reader = sys.stdin.readline
writer = sys.stdout.write

class P11724:
    n_node = None
    n_edge = None
    adjacent = None
    visited = None
    remaining = None

    @staticmethod
    def process_input():
        P11724.n_node, P11724.n_edge = map(int, reader().split())
        P11724.adjacent = {node_index: [] for node_index in range(1, P11724.n_node + 1)}
        P11724.visited = [True] + [False] * P11724.n_node
        P11724.remaining = [node_index for node_index in range(1, P11724.n_node + 1)]
        for _ in range(P11724.n_edge):
            node1, node2 = map(int, reader().split())
            P11724.adjacent[node1].append(node2)
            P11724.adjacent[node2].append(node1)
        return

    @staticmethod
    def bfs(starting_node):
        node_queue = deque([starting_node])
        while node_queue:
            popped_node = node_queue.popleft()
            P11724.visited[popped_node] = True
            P11724.remaining.remove(popped_node)
            for connected_node in P11724.adjacent[popped_node]:
                if not P11724.visited[connected_node] and connected_node not in node_queue:
                    node_queue.append(connected_node)
        return

    @staticmethod
    def execute():
        P11724.process_input()
        count = 0
        while True:
            if P11724.remaining:
                P11724.bfs(P11724.remaining[0])
                count += 1
            else:
                break
        writer(f"{count}\n")
        return

P11724.execute()