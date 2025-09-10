import sys
sys.setrecursionlimit(10**9)
reader = sys.stdin.readline
writer = sys.stdout.write

class P8983:
  number_of_lanes = None
  lanes = None
  number_of_animals = None
  assigned_lane = []
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
    P8983.assigned_lane = [None] * P8983.number_of_animals
    animal_index = 0
    while P8983.x_animals[animal_index] < P8983.lanes[0]:
      P8983.assigned_lane[animal_index] = P8983.lanes[0]
      animal_index += 1
    for closing_lane_index in range(1, P8983.number_of_lanes):
      opening_lane = P8983.lanes[closing_lane_index - 1]
      closing_lane = P8983.lanes[closing_lane_index]
      virtual_center_lane = (opening_lane + closing_lane) // 2
      while P8983.x_animals[animal_index] <= virtual_center_lane:
        P8983.assigned_lane[animal_index] = opening_lane
        animal_index += 1
      while P8983.x_animals[animal_index] < closing_lane:
        P8983.assigned_lane[animal_index] = closing_lane
        animal_index += 1
    while animal_index < P8983.number_of_animals and P8983.lanes[-1] <= P8983.x_animals[animal_index]:
      P8983.assigned_lane[animal_index] = P8983.lanes[-1]
      animal_index += 1

  @staticmethod
  def count_possible():
    counter = 0
    for index in range(P8983.number_of_animals):
      point_x = P8983.x_animals[index]
      point_y = P8983.y_animals[index]
      lane_x = P8983.assigned_lane[index]
      distance = abs(point_x-lane_x) + point_y
      if distance <= P8983.bullet_range:
        counter += 1
    return counter

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
    if P8983.number_of_lanes > 1:
      P8983.assign_lanes()
    elif P8983.number_of_lanes == 1:
      P8983.assigned_lane = [None] * P8983.number_of_animals
      for index_animals in range(P8983.number_of_animals):
        P8983.assigned_lane[index_animals] = P8983.lanes[0]
    # count number of possible targets
    final_answer = P8983.count_possible()

    # writer(f"{P8983.lanes}\n")
    # writer(f"{P8983.x_animals}\n")
    # writer(f"{P8983.y_animals}\n")
    # writer(f"{P8983.assigned_lane}\n")
    # writer(f"{P8983.bullet_range}\n")
    writer(f"{final_answer}\n")

P8983.execute()