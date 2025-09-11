import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P10733:
  @staticmethod
  def execute():
    cardin_readings = int(reader().rstrip())
    stack_box = []
    for _ in range(cardin_readings):
      temp = int(reader().rstrip())
      if temp == 0:
        stack_box.pop()
      else:
        stack_box.append(temp)
    answer = 0
    for item in stack_box:
      answer += item
    writer(f"{answer}\n")
    return

P10733.execute()