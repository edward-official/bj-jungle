import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2110:
  number_of_stalls = None
  number_of_cows = None
  stalls = None

  @staticmethod
  def is_valid(distance):
    # 같은 배열, 같은 거리 조건일 때 구간 선택을 어떻게 하느냐에 따라서 구간 수가 달라질 수 있을까?
    # 1 2 3 4 6 7 8 9 12 13 14 15 19 20 21 22
    temp_distance = 0
    temp_number_of_cows = 1
    for index in range(1, P2110.number_of_stalls):
      if temp_distance == 0:
        if distance <= P2110.stalls[index] - P2110.stalls[index-1]:
          temp_number_of_cows += 1
        else:
          temp_distance += P2110.stalls[index] - P2110.stalls[index-1]
      else:
        temp_distance += P2110.stalls[index] - P2110.stalls[index-1]
        if distance <= temp_distance:
          temp_number_of_cows += 1
          temp_distance = 0
      # writer(f"number of cows until stall[{index}]: {temp_number_of_cows}\n")
      if P2110.number_of_cows <= temp_number_of_cows:
        # writer(f"distance[{distance}]: valid\n")
        return True
    # writer(f"distance[{distance}]: invalid\n")
    return False

  @staticmethod
  def find_answer(opening_distance, closing_distance, recent_answer):
    center_distance = (opening_distance + closing_distance) // 2
    if opening_distance > closing_distance:
      return recent_answer
    elif P2110.is_valid(center_distance):
      recent_answer = center_distance
      return P2110.find_answer(center_distance+1, closing_distance, recent_answer)
    else:
      return P2110.find_answer(opening_distance, center_distance-1, recent_answer)

  @staticmethod
  def execute():
    P2110.number_of_stalls, P2110.number_of_cows = map(int, (reader().rstrip()).split())
    P2110.stalls = [int(reader().rstrip()) for _ in range(P2110.number_of_stalls)]
    P2110.stalls.sort()
    answer = P2110.find_answer(0, P2110.stalls[-1], 1)

    writer(f"{answer}\n")
    return
  
P2110.execute()