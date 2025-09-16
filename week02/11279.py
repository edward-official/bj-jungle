import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def push(self, item):
        self.heap.append(item)
        current_index = len(self.heap) - 1
        while current_index >= 1:
            upper_index = current_index // 2
            if upper_index == 0:
                break
            elif self.heap[upper_index] < self.heap[current_index]:
                temp = self.heap[upper_index]
                self.heap[upper_index] = self.heap[current_index]
                self.heap[current_index] = temp
                current_index = upper_index
            else:
                break

    def pop(self):
        if len(self.heap) == 1:
            return 0
        remember = self.heap.pop(1)
        self.heap.insert(1, self.heap.pop())
        current_index = 1
        while True:
            index1 = current_index * 2
            index2 = current_index * 2 + 1
            if index1 >= len(self.heap):
                # no more nodes left underneath
                break
            elif index2 == len(self.heap) and self.heap[index1] <= self.heap[current_index]:
                # one node left underneath and that one is smaller or equal to the current one
                break
            elif index2 < len(self.heap) and self.heap[index1] <= self.heap[current_index] and self.heap[index2] <= self.heap[current_index]:
                # two more nodes left underneath and they are both smaller or equal to the current one
                break

            if index2 == len(self.heap):
                # one more node left underneath and that one is bigger
                temp = self.heap[current_index]
                self.heap[current_index] = self.heap[index1]
                self.heap[index1] = temp
                break
            elif index2 < len(self.heap) and self.heap[index1] < self.heap[index2]:
                temp = self.heap[current_index]
                self.heap[current_index] = self.heap[index2]
                self.heap[index2] = temp
                current_index = index2
            elif index2 < len(self.heap) and self.heap[index1] >= self.heap[index2]:
                temp = self.heap[current_index]
                self.heap[current_index] = self.heap[index1]
                self.heap[index1] = temp
                current_index = index1
        return remember


class P11279:
    @staticmethod
    def execute():
        max_heap = MaxHeap()
        n_instructions = int(reader())
        for _ in range(n_instructions):
            instruction = int(reader().rstrip())
            if instruction == 0:
                writer(f"{max_heap.pop()}\n")
            else:
                max_heap.push(instruction)
        return

P11279.execute()