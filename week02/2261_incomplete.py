import sys, math
reader = sys.stdin.readline
writer = sys.stdout.write

class P2261:
  x_components = []
  y_components = []
  temp_x = None
  temp_y = None
  current_shortest = math.inf

  @staticmethod
  def merge_components(opening_index, closing_index):
    center_index = (opening_index + closing_index) // 2
    index1 = opening_index
    index2 = center_index + 1
    inserting_index = opening_index
    while index1 <= center_index and index2 <= closing_index:
      if P2261.x_components[index1] <= P2261.x_components[index2]:
        P2261.temp_x[inserting_index] = P2261.x_components[index1]
        P2261.temp_y[inserting_index] = P2261.y_components[index1]
        index1 += 1
      else:
        P2261.temp_x[inserting_index] = P2261.x_components[index2]
        P2261.temp_y[inserting_index] = P2261.y_components[index2]
        index2 += 1
      inserting_index += 1
    while index1 <= center_index:
      P2261.temp_x[inserting_index] = P2261.x_components[index1]
      P2261.temp_y[inserting_index] = P2261.y_components[index1]
      index1 += 1
      inserting_index += 1
    while index2 <= closing_index:
      P2261.temp_x[inserting_index] = P2261.x_components[index2]
      P2261.temp_y[inserting_index] = P2261.y_components[index2]
      index2 += 1
      inserting_index += 1
    
    for index in range(opening_index, closing_index + 1):
      P2261.x_components[index] = P2261.temp_x[index]
      P2261.y_components[index] = P2261.temp_y[index]
    return

  @staticmethod
  def sort_components(opening_index, closing_index):
    if opening_index == closing_index:
      return
    center_index = (opening_index + closing_index) // 2
    P2261.sort_components(opening_index, center_index)
    P2261.sort_components(center_index + 1, closing_index)
    P2261.merge_components(opening_index, closing_index)
    return
  
  @staticmethod
  def catch_answer(opening_index, closing_index):
    center_index = (opening_index + closing_index) // 2
    P2261.catch_answer(opening_index, center_index)
    P2261.catch_answer(center_index + 1, closing_index)
    P2261.current_shortest
    
    return

  @staticmethod
  def execute():
    cardin_components = int(reader().rstrip())
    for _ in range(cardin_components):
      temp_x, temp_y = map(int,(reader().rstrip()).split())
      P2261.x_components.append(temp_x)
      P2261.y_components.append(temp_y)
    P2261.temp_x = [None] * cardin_components
    P2261.temp_y = [None] * cardin_components

    P2261.sort_components(0,cardin_components-1)
    writer(f"{P2261.x_components}\n")
    writer(f"{P2261.y_components}\n")
    return

P2261.execute()