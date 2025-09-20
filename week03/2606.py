import sys
from collections import deque

reader = sys.stdin.readline
writer = sys.stdout.write

class P2606:
    n_computer = None
    n_edge = None
    adjacent = {}

    @staticmethod
    def process_input():
        P2606.n_computer = int(reader())
        P2606.n_edge = int(reader())
        P2606.adjacent = {computer_index: [] for computer_index in range(1, P2606.n_computer+1)}
        for _ in range(P2606.n_edge):
            node1, node2 = map(int, reader().split())
            P2606.adjacent[node1].append(node2)
            P2606.adjacent[node2].append(node1)
        return

    @staticmethod
    def bfs():
        infection_counter = -1
        visited = [False] * (P2606.n_computer + 1)
        computer_queue = deque([1])
        while computer_queue:
            # writer(f"{computer_queue}\n")
            popped_node = computer_queue.popleft()
            infection_counter += 1
            visited[popped_node] = True
            for connected_node in P2606.adjacent[popped_node]:
                if not visited[connected_node] and connected_node not in computer_queue:
                    computer_queue.append(connected_node)
        writer(f"{infection_counter}\n")
        return

    @staticmethod
    def execute():
        P2606.process_input()
        P2606.bfs()
        return

P2606.execute()