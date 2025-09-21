import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P11725:
    n_node = None
    adjacent = None
    dict_parent = None

    @staticmethod
    def process_input():
        P11725.n_node = int(reader())
        P11725.adjacent = {node_index: [] for node_index in range(1, P11725.n_node + 1)}
        P11725.dict_parent = {node_index: [] for node_index in range(2, P11725.n_node + 1)}
        for _ in range(1, P11725.n_node):
            node1, node2 = map(int, reader().split())
            P11725.adjacent[node1].append(node2)
            P11725.adjacent[node2].append(node1)
        return

    @staticmethod
    def find_parent():
        node_queue = deque([1])
        visited = [True] + [False] * P11725.n_node
        visited[1] = True
        while node_queue:
            popped_node = node_queue.popleft()
            visited[popped_node] = True
            for child_node in P11725.adjacent[popped_node]:
                if not visited[child_node]:
                    node_queue.append(child_node)
                    visited[child_node] = True
                    P11725.dict_parent[child_node].append(popped_node)
        for node_index in range(2, P11725.n_node+1):
            writer(f"{P11725.dict_parent[node_index][0]}\n")
        return

    @staticmethod
    def execute():
        P11725.process_input()
        P11725.find_parent()
        return

P11725.execute()
