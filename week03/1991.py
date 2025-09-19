import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P1991:
    n_node = None
    node = None

    @staticmethod
    def process_input():
        P1991.n_node = int(reader())
        P1991.node = [None] * (ord("Z") - ord("A") + 1)
        for _ in range(P1991.n_node):
            n, c1, c2 = map(lambda x: ord(x) - ord("A") if ord(x) >= ord("A") else None, reader().rstrip().split())
            P1991.node[n] = [c1, c2]
        # for index in range(P1991.n_node):
        #     writer(f"{P1991.node[index]}\n")
        return

    @staticmethod
    def _recursive_preorder(node_index):
        l_child, r_child = P1991.node[node_index]
        writer(chr(node_index + ord("A")))
        if l_child:
            P1991._recursive_preorder(l_child)
        if r_child:
            P1991._recursive_preorder(r_child)
        return
    @staticmethod
    def t_preorder():
        P1991._recursive_preorder(0)
        writer("\n")
        return

    @staticmethod
    def _recursive_inorder(node_index):
        l_child, r_child = P1991.node[node_index]
        if l_child:
            P1991._recursive_inorder(l_child)
        writer(chr(node_index + ord("A")))
        if r_child:
            P1991._recursive_inorder(r_child)
        return
    @staticmethod
    def t_inorder():
        P1991._recursive_inorder(0)
        writer("\n")
        return

    @staticmethod
    def _recursive_postorder(node_index):
        l_child, r_child = P1991.node[node_index]
        if l_child:
            P1991._recursive_postorder(l_child)
        if r_child:
            P1991._recursive_postorder(r_child)
        writer(chr(node_index + ord("A")))
        return
    @staticmethod
    def t_postorder():
        P1991._recursive_postorder(0)
        writer("\n")
        return

    @staticmethod
    def execute():
        P1991.process_input()
        P1991.t_preorder()
        P1991.t_inorder()
        P1991.t_postorder()
        return

P1991.execute()