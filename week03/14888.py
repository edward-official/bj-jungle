import sys, math
reader = sys.stdin.readline
writer = sys.stdout.write

class P14888:
    n_operand = None
    operand = None
    operator = None
    operator_stack = []
    answer_big = -math.inf
    answer_small = math.inf

    @staticmethod
    def handle_input():
        P14888.n_operand = int(reader())
        P14888.operand = list(map(int, reader().split()))
        P14888.operator = list(map(int, reader().split()))
        return

    @staticmethod
    def calculate():
        answer = P14888.operand[0]
        for operator_index in range(P14888.n_operand-1):
            if P14888.operator_stack[operator_index] == "+":
                answer += P14888.operand[operator_index+1]
            elif P14888.operator_stack[operator_index] == "-":
                answer -= P14888.operand[operator_index+1]
            elif P14888.operator_stack[operator_index] == "*":
                answer *= P14888.operand[operator_index+1]
            elif P14888.operator_stack[operator_index] == "//":
                answer = int(answer / P14888.operand[operator_index+1])
        return answer

    @staticmethod
    def recursive(n_selected):
        if n_selected == P14888.n_operand - 1:
            calculated = P14888.calculate()
            if P14888.answer_big < calculated:
                P14888.answer_big = calculated
            if calculated < P14888.answer_small:
                P14888.answer_small = calculated
            return
        for selected_operator in range(4):
            if P14888.operator[selected_operator] > 0:
                if selected_operator == 0:
                    P14888.operator_stack.append("+")
                elif selected_operator == 1:
                    P14888.operator_stack.append("-")
                elif selected_operator == 2:
                    P14888.operator_stack.append("*")
                elif selected_operator == 3:
                    P14888.operator_stack.append("//")
                P14888.operator[selected_operator] -= 1
                P14888.recursive(n_selected + 1)
                P14888.operator_stack.pop()
                P14888.operator[selected_operator] += 1
        return

    @staticmethod
    def execute():
        P14888.handle_input()
        P14888.recursive(0)
        writer(f"{P14888.answer_big}\n")
        writer(f"{P14888.answer_small}\n")
        return

P14888.execute()