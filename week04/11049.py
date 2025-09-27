import sys
sys.setrecursionlimit(10**6)
reader = sys.stdin.readline
writer = sys.stdout.write

class P11049:
  n_matrix = None
  rc = None
  dynamic = None

  @staticmethod
  def process_input():
    P11049.n_matrix = int(reader())
    P11049.rc = []
    r, c = map(int, reader().split())
    P11049.rc.append(r)
    P11049.rc.append(c)
    for _ in range(P11049.n_matrix - 1):
      _r, _c = map(int, reader().split())
      P11049.rc.append(_c)
    P11049.dynamic = [[0 for _ in range(P11049.n_matrix + 1)] for _ in range(P11049.n_matrix + 1)]
    return

  @staticmethod
  def execute():
    P11049.process_input()
    if P11049.n_matrix <= 1:
      writer("0\n")
      return
    positive_inf = 10**30
    for length in range(2, P11049.n_matrix + 1):
      for opening_index in range(1, P11049.n_matrix - length + 2):
        closing_index = opening_index + length - 1
        minimum = positive_inf
        for dividing_index in range(opening_index, closing_index):
          temp = P11049.dynamic[opening_index][dividing_index] + P11049.dynamic[dividing_index + 1][closing_index] + P11049.rc[opening_index - 1] * P11049.rc[dividing_index] * P11049.rc[closing_index]
          if temp < minimum:
            minimum = temp
        P11049.dynamic[opening_index][closing_index] = minimum

    writer(f"{P11049.dynamic[1][P11049.n_matrix]}\n")
    return

P11049.execute()
