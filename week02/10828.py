import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P10828:
  @staticmethod
  def execute():
    cardin_instructions = int(reader().rstrip())
    stack_box = []
    for _ in range(cardin_instructions):
      instruction = (reader().rstrip()).split()
      if instruction[0] == "push":
        stack_box.append(int(instruction[1]))
      elif instruction[0] == "pop":
        if stack_box:
          writer(f"{stack_box.pop()}\n")
        else:
          writer("-1\n")
      elif instruction[0] == "size":
        writer(f"{len(stack_box)}\n")
      elif instruction[0] == "empty":
        if not stack_box:
          writer("1\n")
        else:
          writer("0\n")
      elif instruction[0] == "top":
        if stack_box:
          writer(f"{stack_box[-1]}\n")
        else:
          writer("-1\n")
    return

P10828.execute()