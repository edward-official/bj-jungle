import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P11053:
  number_of_received = None
  received = None
  rear = []

  @staticmethod
  def compute_position(target, opening_index, closing_index):
    center_index = (opening_index + closing_index) // 2
    if closing_index < opening_index:
      return (opening_index + 1) * (-1)
    
    if target == P11053.rear[center_index]:
      return center_index
    elif target < P11053.rear[center_index]:
      return P11053.compute_position(target, opening_index, center_index-1)
    else:
      return P11053.compute_position(target, center_index+1, closing_index)

  @staticmethod
  def compute_answer():
    for index in range(P11053.number_of_received):
      target = P11053.received[index]
      if not P11053.rear:
        P11053.rear.append(target)
        continue
      elif len(P11053.rear) == 1:
        if target < P11053.rear[0]:
          P11053.rear[0] = target
        elif P11053.rear[0] < target:
          P11053.rear.append(target)
        continue
      else:
        if target < P11053.rear[0]:
          P11053.rear[0] = target
          continue
        elif P11053.rear[-1] < target:
          P11053.rear.append(target)
          continue

      position = P11053.compute_position(target, 0, len(P11053.rear)-1)
      if position < 0:
        position = (position + 1) * (-1)
      
      if position == len(P11053.rear):
        P11053.rear.append(target)
      elif target < P11053.rear[position]:
        P11053.rear[position] = target
      # writer(f"{P11053.rear}: {position}\n")
    return

  @staticmethod
  def execute():
    P11053.number_of_received = int(reader().rstrip())
    P11053.received = list(map(int, (reader().rstrip()).split()))
    P11053.compute_answer()

    writer(f"{len(P11053.rear)}\n")

P11053.execute()
