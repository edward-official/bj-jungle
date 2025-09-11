import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2493:
  @staticmethod
  def execute():
    cardin_readings = int(reader().rstrip())
    heights = list(map(int,(reader().rstrip()).split()))
    stack_index = []
    answer = []
    for index in range(cardin_readings):
      temp_height = heights[index]
      while stack_index and heights[stack_index[-1]] < temp_height:
        stack_index.pop()
      if stack_index:
        answer.append(stack_index[-1]+1)
      else:
        answer.append(0)
      stack_index.append(index)
    for item in answer:
      writer(f"{item} ")
    writer("\n")
    return

P2493.execute()