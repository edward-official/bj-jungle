import sys
from collections import deque

reader = sys.stdin.readline
writer = sys.stdout.write

class P21606:
    n_node = None
    n_edge = None
    adjacent = None
    indoor_mark = None
    remaining_indoor = None

    @staticmethod
    def is_indoor(target_node):
        if P21606.indoor_mark[target_node-1] == "1":
            return True
        return False

    @staticmethod
    def process_input():
        P21606.n_node = int(reader())
        P21606.n_edge = P21606.n_node - 1
        P21606.adjacent = {node_index: [] for node_index in range(1, P21606.n_node + 1)}
        P21606.indoor_mark = reader().rstrip()
        P21606.remaining_indoor = []
        for _ in range(P21606.n_edge):
            node1, node2 = map(int, reader().split())
            P21606.adjacent[node1].append(node2)
            P21606.adjacent[node2].append(node1)
        for index, mark in enumerate(P21606.indoor_mark):
            if mark == "1":
                P21606.remaining_indoor.append(index+1)
        P21606.remaining_indoor.sort()
        return

    @staticmethod
    def count():
        """
        while remaining_indoor
            remaining_indoor에서 하나를 가져옴
            그 점에서 출발해서 bfs시작
            indoor인 점을 만나면 멈추기
            if remember에 없다:
                count += 1
                remember.append((index1, index2))
        """
        remember = []
        count = 0
        while P21606.remaining_indoor:
            opening_indoor = P21606.remaining_indoor.pop(0)
            node_queue = deque([opening_indoor])
            visited = [False] * (P21606.n_node + 1)
            visited[opening_indoor] = True
            while node_queue:
                popped_node = node_queue.popleft()
                if P21606.is_indoor(popped_node) and opening_indoor != popped_node:
                    if (opening_indoor, popped_node) in remember:
                        continue
                    else:
                        # writer(f"opening_indoor: {opening_indoor}, closing_indoor: {popped_node}\n")
                        count += 1
                        remember.append((opening_indoor, popped_node))
                        continue
                for adjacent_node in P21606.adjacent[popped_node]:
                    if not visited[adjacent_node]:
                        node_queue.append(adjacent_node)
                        visited[adjacent_node] = True
        writer(f"{count}\n")
        return

    @staticmethod
    def execute():
        P21606.process_input()
        P21606.count()
        return

P21606.execute()