import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P18258:
    @staticmethod
    def execute():
        n_instructions = int(reader())
        queue_box = deque()
        for _ in range(n_instructions):
            components = reader().rstrip().split()
            if components[0] == 'push':
                queue_box.append(int(components[1]))
            elif components[0] == 'pop':
                if queue_box:
                    writer(f"{queue_box.popleft()}\n")
                else:
                    writer("-1\n")
            elif components[0] == 'size':
                writer(f"{len(queue_box)}\n")
            elif components[0] == 'empty':
                if queue_box:
                    writer("0\n")
                else:
                    writer("1\n")
            elif components[0] == 'front':
                if queue_box:
                    writer(f"{queue_box[0]}\n")
                else:
                    writer("-1\n")
            elif components[0] == 'back':
                if queue_box:
                    writer(f"{queue_box[-1]}\n")
                else:
                    writer("-1\n")
        return

P18258.execute()