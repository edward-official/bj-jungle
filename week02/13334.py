import heapq
import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P13334:
    @staticmethod
    def execute():
        n_people = int(reader().rstrip())
        informations = []
        for _ in range(n_people):
            h, o = map(int, reader().rstrip().split())
            informations.append([min(h, o), max(h, o)])
        distance = int(reader().rstrip())
        candidates = [information for information in informations if information[1] - information[0] <= distance]
        candidates.sort(key=lambda candidate: (candidate[1], candidate[0]))
        minheap = []
        answer = 0
        for left, right in candidates:
            heapq.heappush(minheap, left)
            while minheap and minheap[0] < right - distance:
                heapq.heappop(minheap)
            if answer < len(minheap):
                answer = len(minheap)
        writer(f"{answer}\n")
        return

P13334.execute()