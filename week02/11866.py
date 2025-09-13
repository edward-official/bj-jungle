import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P11866:
    @staticmethod
    def execute():
        n_people, k = map(int, reader().rstrip().split())
        queue_box = deque()
        for item in range(1, n_people + 1):
            queue_box.append(item)
        deleting_index = k-1
        deleting_item = queue_box[deleting_index]
        queue_box.remove(deleting_item)
        writer(f"<{deleting_item}")
        while queue_box:
            deleting_index = (deleting_index + k - 1) % len(queue_box)
            deleting_item = queue_box[deleting_index]
            queue_box.remove(deleting_item)
            writer(f", {deleting_item}")
        writer(">\n")
        return

P11866.execute()