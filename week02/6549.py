import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P6549:
  @staticmethod
  def compute_area(cardin_components, components):
    stack = []
    current_best = 0

    for current_index in range(cardin_components + 1):
      current_component = components[current_index] if current_index < cardin_components else 0
      while stack and components[stack[-1]] > current_component:
        popped_index = stack.pop()
        popped_height = components[popped_index]
        limit_left = stack[-1] + 1 if stack else 0
        width = current_index - limit_left
        temp_area = popped_height * width
        if temp_area > current_best:
          current_best = temp_area
      stack.append(current_index)
    return current_best

  @staticmethod
  def execute():
    while True:
      received = list(map(int, reader().rstrip().split()))
      if received[0] == 0:
        break
      else:
        cardin_components = received[0]
        components = received[1:]
        answer = P6549.compute_area(cardin_components, components)
        writer(f"{answer}\n")
    return

P6549.execute()
