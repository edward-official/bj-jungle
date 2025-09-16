import sys
from collections import deque
reader = sys.stdin.readline
writer = sys.stdout.write

class P3190:
    width = None
    snake_tracer = deque()
    direction = 3
    second_passed = 0
    apples = []
    turns = []

    @staticmethod
    def update_direction():
        for turn in P3190.turns:
            if turn[0] == P3190.second_passed:
                P3190.direction = (P3190.direction + turn[1]) % 12
                P3190.turns.remove(turn)
                break
        return

    @staticmethod
    def next_point():
        current_point = [P3190.snake_tracer[-1][0], P3190.snake_tracer[-1][1]]
        if P3190.direction == 0:
            return [current_point[0] - 1, current_point[1]]
        elif P3190.direction == 3:
            return [current_point[0], current_point[1] + 1]
        elif P3190.direction == 6:
            return [current_point[0] + 1, current_point[1]]
        elif P3190.direction == 9:
            return [current_point[0], current_point[1] - 1]

    @staticmethod
    def check_collision(r, c):
        if [r,c] in P3190.snake_tracer:
            return True
        elif r < 0 or c < 0 or r >= P3190.width or c >= P3190.width:
            return True
        else:
            return False

    @staticmethod
    def check_apple():
        current_r = P3190.snake_tracer[-1][0]
        current_c = P3190.snake_tracer[-1][1]
        for apple in P3190.apples:
            if apple[0] == current_r and apple[1] == current_c:
                P3190.apples.remove(apple)
                return True
        return False

    @staticmethod
    def process_input():
        P3190.width = int(reader())
        n_apples = int(reader())
        for _ in range(n_apples):
            r, c = map(int, reader().rstrip().split())
            P3190.apples.append([r-1, c-1])
        n_turns = int(reader())
        for _ in range(n_turns):
            time, direction = reader().rstrip().split()
            time = int(time)
            direction = 3 if direction == "D" else -3
            P3190.turns.append([time, direction])
        P3190.snake_tracer.append([0,0])
        return

    @staticmethod
    def execute():
        """
        일단 뱀이 존재하는 모든 점들을 큐에 담아서 관리
        진행방향을 관리하면서 매 초마다 진행방향으로 진행 + 사과의 존재 유무 확인

        while True:
            clock_second += 1
            방향을 바꿔야하는지 체크하고 방향 업데이트
            충돌 여부 확인 > 1칸 진행 || 반복문 탈출
            사과를 확인하고 사과가 없으면 꼬리 자르기
        시간 출력
        """
        P3190.process_input()
        while True:
            P3190.second_passed += 1
            next_point = P3190.next_point()
            if P3190.check_collision(next_point[0], next_point[1]):
                break
            else:
                P3190.snake_tracer.append(next_point)
            if not P3190.check_apple():
                P3190.snake_tracer.popleft()
            P3190.update_direction()

        writer(f"{P3190.second_passed}\n")
        # writer(f"{P3190.width}\n")
        # writer(f"{P3190.turns}\n")
        # writer(f"{P3190.apples}\n")
        return

P3190.execute()