import sys, math
reader = sys.stdin.readline
writer = sys.stdout.write

class P2470:
  number_of_elements = None
  elements = None

  @staticmethod
  def find_index2(recent_minimum, recent_index2, index1, opening_index, closing_index):
    if opening_index > closing_index:
      return [recent_minimum, recent_index2]
    center_index = (opening_index + closing_index) // 2
    summation = P2470.elements[index1] + P2470.elements[center_index]
    absoluted = abs(summation)
    if absoluted < recent_minimum:
      recent_minimum = absoluted
      recent_index2 = center_index

    if summation == 0:
      return [0, center_index]
    elif summation < 0:
      return P2470.find_index2(recent_minimum, recent_index2, index1, center_index+1, closing_index)
    else:
      return P2470.find_index2(recent_minimum, recent_index2, index1, opening_index, center_index-1)

  @staticmethod
  def find_answer():
    current_optimal = math.inf
    current_index1 = None
    current_index2 = None
    for index1 in range(P2470.number_of_elements):
      regional_optimal, index2 = P2470.find_index2(math.inf, None, index1, index1+1, len(P2470.elements)-1)
      if regional_optimal < current_optimal:
        current_optimal = regional_optimal
        current_index1 = index1
        current_index2 = index2
    return [current_index1, current_index2]

  @staticmethod
  def execute():
    P2470.number_of_elements = int(reader().rstrip("\n"))
    P2470.elements = list(map(int,(reader().rstrip("\n")).split()))
    P2470.elements.sort()

    index1, index2 = P2470.find_answer()
    writer(f"{P2470.elements[index1]} {P2470.elements[index2]}\n")

P2470.execute()