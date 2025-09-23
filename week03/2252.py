from collections import deque
import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2252:
    n_student = 0
    n_comparison = 0
    follower = None
    relative_order = None
    heading_student = None

    @staticmethod
    def process_input():
        P2252.n_student, P2252.n_comparison = map(int, reader().split())
        P2252.follower = {student_index: [] for student_index in range(1, P2252.n_student + 1)}
        P2252.relative_order = [0] * (P2252.n_student + 1)
        P2252.heading_student = deque()
        for _ in range(P2252.n_comparison):
            student1, student2 = map(int, reader().split())
            P2252.follower[student1].append(student2)
            P2252.relative_order[student2] += 1
        for student_index in range(1, P2252.n_student + 1):
            if P2252.relative_order[student_index] == 0:
                P2252.heading_student.append(student_index)
        return

    @staticmethod
    def bfs():
        answer = []
        while P2252.heading_student:
            heading_student = P2252.heading_student.popleft()
            answer.append(heading_student)
            for follower_student in P2252.follower[heading_student]:
                P2252.relative_order[follower_student] -= 1
                if P2252.relative_order[follower_student] == 0:
                    P2252.heading_student.append(follower_student)
        writer(f"{' '.join(map(str, answer))}\n")
        return

    @staticmethod
    def execute():
        P2252.process_input()
        P2252.bfs()

P2252.execute()
