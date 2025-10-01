import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P2637:
    complete_product_index = None
    n_topology = None
    topology = None
    indegree = None
    required_basic_components = None

    @staticmethod
    def stdin_processor():
        P2637.complete_product_index = int(reader())
        P2637.n_topology = int(reader())
        P2637.topology = [[] for _ in range(P2637.complete_product_index + 1)]
        P2637.indegree = [0] * (P2637.complete_product_index + 1)
        for _ in range(P2637.n_topology):
            compound_index, component_index, quantity = map(int, reader().split())
            P2637.topology[component_index].append((compound_index, quantity))
            P2637.indegree[compound_index] += 1
        P2637.required_basic_components = [[0 for _ in range(P2637.complete_product_index + 1)] for _ in range(P2637.complete_product_index + 1)]
        return

    @staticmethod
    def analyse_topology():
        product_queue = deque()
        for product_index in range(1, P2637.complete_product_index + 1):
            if P2637.indegree[product_index] == 0:
                P2637.required_basic_components[product_index][product_index] = 1
                product_queue.append(product_index)
        while product_queue:
            component_index = product_queue.popleft()
            for compound_index, quantity in P2637.topology[component_index]:
                for traverse in range(1, P2637.complete_product_index + 1):
                    if P2637.required_basic_components[component_index][traverse] > 0:
                        P2637.required_basic_components[compound_index][traverse] += (
                            P2637.required_basic_components[component_index][traverse] * quantity
                        )
                P2637.indegree[compound_index] -= 1
                if P2637.indegree[compound_index] == 0:
                    product_queue.append(compound_index)
        return

    @staticmethod
    def stdout_answer():
        for traverse in range(1, P2637.complete_product_index + 1):
            if P2637.required_basic_components[P2637.complete_product_index][traverse] > 0:
                writer(f"{traverse} {P2637.required_basic_components[P2637.complete_product_index][traverse]}\n")
        return

    @staticmethod
    def execute():
        P2637.stdin_processor()
        P2637.analyse_topology()
        P2637.stdout_answer()
        return

P2637.execute()
