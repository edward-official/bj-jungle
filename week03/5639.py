import sys
sys.setrecursionlimit(10**6)
reader = sys.stdin.readline
writer = sys.stdout.write

class P5639:
    adjacent_tree = [[] for _ in range(10**6)] # have to be changed to dictionary!!
    root_node = None

    @staticmethod
    def process_input():
        P5639.root_node = int(reader().rstrip())
        t_stack = [P5639.root_node]
        while True:
            received = reader()
            if not received or not received.rstrip():
                break

            received = int(received.rstrip())
            if received < t_stack[-1]:
                P5639.adjacent_tree[t_stack[-1]].append(received)
                t_stack.append(received)
            elif received > t_stack[-1]:
                target_node = None
                while t_stack and t_stack[-1] < received:
                    target_node = t_stack.pop()
                P5639.adjacent_tree[target_node].append(received)
                t_stack.append(received)

        # for index, at in enumerate(P5639.adjacent_tree):
        #     if at:
        #         writer(f"[{index}]: {at}\n")
        return

    @staticmethod
    def _postorder_recursive(node_index):
        if not P5639.adjacent_tree[node_index]:
            pass
        elif len(P5639.adjacent_tree[node_index]) == 1:
            child_l = P5639.adjacent_tree[node_index][0]
            P5639._postorder_recursive(child_l)
        elif len(P5639.adjacent_tree[node_index]) == 2:
            child_l, child_r = P5639.adjacent_tree[node_index]
            P5639._postorder_recursive(child_l)
            P5639._postorder_recursive(child_r)
        writer(f"{node_index}\n")
        return
    @staticmethod
    def t_postorder():
        P5639._postorder_recursive(P5639.root_node)
        writer("\n")
        return

    @staticmethod
    def execute():
        P5639.process_input()
        P5639.t_postorder()
        return

P5639.execute()