import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P2110:
    @staticmethod
    def execute():
        n_card = int(reader())
        queue_box = deque()
        for item in range(1, n_card + 1):
            queue_box.append(item)
        while len(queue_box) != 1:
            queue_box.popleft()
            if queue_box:
                queue_box.append(queue_box.popleft())
        writer(f"{queue_box[0]}\n")
        return

P2110.execute()