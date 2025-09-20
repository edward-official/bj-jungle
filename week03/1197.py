import sys, heapq
reader = sys.stdin.readline
writer = sys.stdout.write

class P1197:
    n_node = 0
    n_edge = 0
    adjacent = {}

    @staticmethod
    def prim(start):
        visited = [False] * (P1197.n_node + 1)
        minimum_queue = []
        accumulated_weight = 0
        edge_counter = 0
        visited[start] = True
        for connected_node, w in P1197.adjacent[start]:
            heapq.heappush(minimum_queue, (w, connected_node))
        while minimum_queue and edge_counter < P1197.n_node - 1:
            # 큐에서 간선들을 하나씩 확인 > 사이클을 만들지 않는 간선을 찾고 업데이트 > 다음 점으로 이동
            w, connected_node = heapq.heappop(minimum_queue)
            if visited[connected_node]:
                continue
            visited[connected_node] = True
            accumulated_weight += w
            edge_counter += 1
            for pushing_node, pushing_weight in P1197.adjacent[connected_node]:
                if not visited[pushing_node]:
                    heapq.heappush(minimum_queue, (pushing_weight, pushing_node))
        return accumulated_weight

    @staticmethod
    def execute():
        P1197.n_node, P1197.n_edge = map(int, reader().split())
        P1197.adjacent = {node_index: [] for node_index in range(1, P1197.n_node + 1)}
        for _ in range(P1197.n_edge):
            node1, node2, weight = map(int, reader().split())
            P1197.adjacent[node1].append((node2, weight))
            P1197.adjacent[node2].append((node1, weight))
        writer(f"{P1197.prim(1)}\n")
        return

P1197.execute()
