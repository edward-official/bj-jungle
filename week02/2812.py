import sys, copy
reader = sys.stdin.readline
writer = sys.stdout.write

class P2812:
  given_data = None
  modified_data = None
  modified_index = None
  depot_data = None
  depot_index = None

  @staticmethod
  def merge(opening_index, closing_index):
    center_index = (opening_index + closing_index) // 2
    index1 = opening_index
    index2 = center_index + 1
    inserting_index = opening_index
    while index1 <= center_index and index2 <= closing_index:
      if P2812.modified_data[index1] >= P2812.modified_data[index2]:
        P2812.depot_data[inserting_index] = P2812.modified_data[index1]
        P2812.depot_index[inserting_index] = P2812.modified_index[index1]
        index1 += 1
        inserting_index += 1
      else:
        P2812.depot_data[inserting_index] = P2812.modified_data[index2]
        P2812.depot_index[inserting_index] = P2812.modified_index[index2]
        index2 += 1
        inserting_index += 1
    while index1 <= center_index:
      P2812.depot_data[inserting_index] = P2812.modified_data[index1]
      P2812.depot_index[inserting_index] = P2812.modified_index[index1]
      index1 += 1
      inserting_index += 1
    while index2 <= closing_index:
      P2812.depot_data[inserting_index] = P2812.modified_data[index2]
      P2812.depot_index[inserting_index] = P2812.modified_index[index2]
      index2 += 1
      inserting_index += 1
    for index in range(opening_index, closing_index + 1):
      P2812.modified_data[index] = P2812.depot_data[index]
      P2812.modified_index[index] = P2812.depot_index[index]
    return

  @staticmethod
  def mergesort(opening_index, closing_index):
    center_index = (opening_index + closing_index) // 2
    if opening_index == closing_index:
      return
    P2812.mergesort(opening_index, center_index)
    P2812.mergesort(center_index+1, closing_index)
    P2812.merge(opening_index, closing_index)
    return
  
  @staticmethod
  def execute():
    given_length, removing_length = map(int, (reader().rstrip()).split())
    P2812.given_data = list(map(int,reader().rstrip("\n")))

    P2812.modified_data = copy.deepcopy(P2812.given_data)
    P2812.modified_index = [index for index in range(given_length)]
    P2812.depot_data = [None] * given_length
    P2812.depot_index = [None] * given_length

    """
    7 - 2 == 5
    when selecting answer index n (n+1 th) there should be at least (required_n - n -1) items
    0  1  2  3  4  (5) (6)
    """

    P2812.mergesort(0,given_length-1)
    # writer(f"\n")
    # writer(f"{P2812.given_data}\n")
    # writer(f"{P2812.modified_data}\n")
    # writer(f"{P2812.modified_index}\n")
    # writer(f"\n")

    used_marking = -1
    required_length = given_length - removing_length
    answer = [0] * required_length
    for answer_inserting_index in range(required_length):
      traverse_modified = 0
      possible_limit = given_length - (required_length - answer_inserting_index)
      # writer(f"💻 inserting answer on index {answer_inserting_index}\n")
      # writer(f"💻 current answer: {answer}, used marking: {used_marking}, possible limit: {possible_limit}\n")
      while True:
        original_index = P2812.modified_index[traverse_modified]
        # writer(f"checking data {P2812.modified_data[traverse_modified]} from index {original_index}\n")
        if used_marking <  original_index and original_index <= possible_limit:
          used_marking = original_index
          answer[answer_inserting_index] = P2812.modified_data[traverse_modified]
          break
        traverse_modified += 1
    writer(f"{answer}\n")
    for item in answer:
      writer(f"{item}")
    writer("\n")
    return

P2812.execute()