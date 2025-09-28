import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P11053:
    n_items = None
    items = None
    tails = None

    @staticmethod
    def process_input():
        P11053.n_items = int(reader())
        P11053.items = list(map(int, reader().split()))
        P11053.tails = [-1]
        return

    @staticmethod
    def process_item(item):
        # -1 1 3 7 10 < 0
        if P11053.tails[-1] < item:
            P11053.tails.append(item)
            return
        for index in range(len(P11053.tails) - 2, -1, -1):
            if P11053.tails[index] < item:
                P11053.tails[index + 1] = item
                break
        return

    @staticmethod
    def compute():
        for item in P11053.items:
            P11053.process_item(item)
        writer(f"{len(P11053.tails)-1}\n")
        return

    @staticmethod
    def execute():
        P11053.process_input()
        P11053.compute()
        return

P11053.execute()