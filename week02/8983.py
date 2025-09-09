import sys
sys.setrecursionlimit(10**9)
reader = sys.stdin.readline
writer = sys.stdout.write

class P8983:
  number_of_lanes = None
  lanes = None
  number_of_animals = None
  x_animals = []
  y_animals = []
  x_temp = []
  y_temp = []
  bullet_range = None

  @staticmethod
  def merge_components(opening_index, closing_index):
    center_index = (opening_index + closing_index) // 2
    index1 = opening_index
    index2 = center_index + 1
    inserting_index = opening_index

    while index1 <= center_index and index2 <= closing_index:
      if P8983.x_animals[index1] <= P8983.x_animals[index2]:
        P8983.x_temp[inserting_index] = P8983.x_animals[index1]
        P8983.y_temp[inserting_index] = P8983.y_animals[index1]
        index1 += 1
        inserting_index += 1
      else:
        P8983.x_temp[inserting_index] = P8983.x_animals[index2]
        P8983.y_temp[inserting_index] = P8983.y_animals[index2]
        index2 += 1
        inserting_index += 1
    
    while index1 <= center_index:
      P8983.x_temp[inserting_index] = P8983.x_animals[index1]
      P8983.y_temp[inserting_index] = P8983.y_animals[index1]
      index1 += 1
      inserting_index += 1
    
    while index2 <= closing_index:
      P8983.x_temp[inserting_index] = P8983.x_animals[index2]
      P8983.y_temp[inserting_index] = P8983.y_animals[index2]
      index2 += 1
      inserting_index += 1
    
    for index in range(opening_index, closing_index + 1):
      P8983.x_animals[index] = P8983.x_temp[index]
      P8983.y_animals[index] = P8983.y_temp[index]
    
    return

  @staticmethod
  def sort_animals(opening_index, closing_index):
    if opening_index == closing_index:
      return
    center_index = (opening_index + closing_index) // 2
    P8983.sort_animals(opening_index, center_index)
    P8983.sort_animals(center_index+1, closing_index)
    P8983.merge_components(opening_index, closing_index)
    return

  @staticmethod
  def assign_lanes():
    opening_index_lane = 0
    closing_index_lane = 1
    index_animal = 0

  @staticmethod
  def execute():
    P8983.number_of_lanes, P8983.number_of_animals, P8983.bullet_range = map(int, (reader().rstrip()).split())
    P8983.lanes = list(map(int,(reader().rstrip()).split()))
    for _ in range(P8983.number_of_animals):
      x, y = map(int,(reader().rstrip()).split())
      P8983.x_animals.append(x)
      P8983.y_animals.append(y)

    P8983.lanes.sort()
    P8983.x_temp = [None] * P8983.number_of_animals
    P8983.y_temp = [None] * P8983.number_of_animals
    P8983.sort_animals(0,P8983.number_of_animals-1)

    writer(f"{P8983.lanes}\n")
    writer(f"{P8983.x_animals}\n")
    writer(f"{P8983.y_animals}\n")
    writer(f"{P8983.bullet_range}\n")

P8983.execute()