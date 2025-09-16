import sys, heapq
reader = sys.stdin.readline
writer = sys.stdout.write

class P1715:
    heap_box = []
    answer = 0

    @staticmethod
    def execute():
        n_inputs = int(reader().rstrip())
        for _ in range(n_inputs):
            input = int(reader().rstrip())
            heapq.heappush(P1715.heap_box, input)
        if len(P1715.heap_box) == 1:
            writer(f"{P1715.answer}\n")
            return
        while len(P1715.heap_box) >= 2:
            popped1 = heapq.heappop(P1715.heap_box)
            popped2 = heapq.heappop(P1715.heap_box)
            heapq.heappush(P1715.heap_box, popped1 + popped2)
            P1715.answer += (popped1 + popped2)
        writer(f"{P1715.answer}\n")
        return

P1715.execute()