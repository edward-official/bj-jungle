import sys
reader = sys.stdin.readline
writer = sys.stdout.write


class P1920:
  @staticmethod
  def is_member(sorted_elements, target, opening_index, closing_index):
    if opening_index == closing_index:
      if sorted_elements[opening_index] != target:
        return False
      else:
        return True
    elif opening_index + 1 == closing_index:
      if sorted_elements[opening_index] != target and sorted_elements[closing_index] != target:
        return False
      else:
        return True
    center_index = (opening_index + closing_index) // 2
    if sorted_elements[center_index] == target:
      return True
    elif target < sorted_elements[center_index]:
      return P1920.is_member(sorted_elements, target, opening_index, center_index-1)
    else:
      return P1920.is_member(sorted_elements, target, center_index+1, closing_index)

  @staticmethod
  def execute():
    number_of_elements = int(reader().rstrip("\n"))
    elements = list(map(int,(reader().rstrip()).split()))
    number_of_targets = int(reader().rstrip("\n"))
    targets = list(map(int,(reader().rstrip()).split()))

    elements.sort()

    for index in range(number_of_targets):
      if P1920.is_member(elements, targets[index], 0, number_of_elements-1):
        print("1")
      else:
        print("0")


P1920.execute()