import sys
from collections import deque

reader = sys.stdin.readline
writer = sys.stdout.write

class P1707:
    n_node = None
    n_edge = None
    adjacent = None
    visited = None
    remaining_node = None
    team_mark = None

    @staticmethod
    def process_input():
        P1707.n_node, P1707.n_edge = map(int, reader().split())
        P1707.adjacent = {node_index: [] for node_index in range(1, P1707.n_node + 1)}
        P1707.visited = [False] * (P1707.n_node + 1)
        P1707.remaining_node = [node_index for node_index in range(1, P1707.n_node + 1)]
        P1707.team_mark = [None] * (P1707.n_node + 1)
        for _ in range(P1707.n_edge):
            node1, node2 = map(int, reader().split())
            P1707.adjacent[node1].append(node2)
            P1707.adjacent[node2].append(node1)
        return

    @staticmethod
    def _assign_team(starting_node):
        node_queue = deque([starting_node])
        P1707.visited[starting_node] = True
        P1707.team_mark[starting_node] = True
        P1707.remaining_node.remove(starting_node)
        # writer(f"starting_node = {starting_node}\n")
        while node_queue:
            popped_node = node_queue.popleft()
            for adjacent_node in P1707.adjacent[popped_node]:
                # writer(f"{P1707.team_mark} popped_node = {popped_node}, adjacent_node = {adjacent_node}\n")
                if not P1707.visited[adjacent_node]:
                    node_queue.append(adjacent_node)
                    P1707.visited[adjacent_node] = True
                    P1707.team_mark[adjacent_node] = not P1707.team_mark[popped_node]
                    P1707.remaining_node.remove(adjacent_node)
                elif P1707.visited[adjacent_node] and P1707.team_mark[popped_node] == P1707.team_mark[adjacent_node]:
                    return False
        # writer(f"{P1707.team_mark}\n")
        return True

    @staticmethod
    def assign_team():
        while P1707.remaining_node:
            if not P1707._assign_team(P1707.remaining_node[0]):
                writer("NO\n")
                return
        writer("YES\n")
        return

    @staticmethod
    def testcase():
        P1707.process_input()
        P1707.assign_team()
        """
        일단 모든 점을 탐색하면서 점에 팀 번호를 표시한다.
        탐색하지 않은 점들의 정보를 추적하기 위해서 노드 배열을 하나 만들고 탐색된 점들은 제거한다.
        bfs를 반복하면서 점들에 팀 번호를 배정하고 번호가 충돌한다면 즉시 결과를 출력하고 메서드를 종료한다.
        """
        return

    @staticmethod
    def execute():
        n_testcase = int(reader())
        for _ in range(n_testcase):
            P1707.testcase()
        return

P1707.execute()