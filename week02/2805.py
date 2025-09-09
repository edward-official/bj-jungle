import sys
# sys.setrecursionlimit(1_000_000_000)
reader = sys.stdin.readline
writer = sys.stdout.write

class P2805:
  @staticmethod
  def compute_amount(number_of_trees, sorted_trees, height):
    amount = 0
    for index in range(number_of_trees):
      if height < sorted_trees[index]:
        amount += (sorted_trees[index] - height)
    return amount

  @staticmethod
  def find_answer(number_of_trees, sorted_trees, target_amount, opening_height, closing_height, answer_height):
    center_height = (opening_height + closing_height) // 2
    amount = P2805.compute_amount(number_of_trees, sorted_trees, center_height)
    if opening_height > closing_height:
      return answer_height
    elif amount < target_amount:
      return P2805.find_answer(number_of_trees, sorted_trees, target_amount, opening_height, center_height-1, answer_height)
    else:
      if answer_height < center_height:
        answer_height = center_height
      return P2805.find_answer(number_of_trees, sorted_trees, target_amount, center_height+1, closing_height, answer_height)

  @staticmethod
  def execute():
    number_of_trees, target_amount = map(int, (reader().rstrip()).split())
    trees = list(map(int,(reader().rstrip()).split()))
    trees.sort()
    print(P2805.find_answer(number_of_trees,trees,target_amount,0,trees[-1],0))
    return

P2805.execute()
