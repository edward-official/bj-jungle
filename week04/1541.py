import sys, re
reader = sys.stdin.readline
writer = sys.stdout.write

class P1541:
    expression = None
    operators = None
    operands = None

    @staticmethod
    def stdin_processor():
        P1541.expression = reader().strip()
        P1541.operators = []
        for index in range(1, len(P1541.expression)):
            if P1541.expression[index] == '+' or P1541.expression[index] == '-':
                P1541.operators.append(P1541.expression[index])
        P1541.operands = list(map(int, re.split("[+-]", P1541.expression)))
        return

    @staticmethod
    def execute():
        P1541.stdin_processor()
        answer = P1541.operands[0]
        adding_procedure = True
        for operator_index in range(len(P1541.operators)):
            if adding_procedure and P1541.operators[operator_index] == '+':
                answer += P1541.operands[operator_index + 1]
            elif adding_procedure and P1541.operators[operator_index] == '-':
                answer -= P1541.operands[operator_index + 1]
                adding_procedure = False
            elif not adding_procedure:
                answer -= P1541.operands[operator_index + 1]
        writer(f"{answer}\n")
        return

P1541.execute()