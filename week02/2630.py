import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2630:
  width = None
  board = None
  counter0 = 0
  counter1 = 0

  @staticmethod
  def is_mixed(width, opening_row, opening_column):
    expected = P2630.board[opening_row][opening_column]
    for row in range(opening_row, opening_row + width):
      for column in range(opening_column, opening_column + width):
        if P2630.board[row][column] != expected:
          return True
    return False
  
  @staticmethod
  def compute_zone(width, opening_row, opening_column):
    if P2630.is_mixed(width, opening_row, opening_column):
      width = width // 2
      P2630.compute_zone(width, opening_row, opening_column)
      P2630.compute_zone(width, opening_row, opening_column + width)
      P2630.compute_zone(width, opening_row + width, opening_column)
      P2630.compute_zone(width, opening_row + width, opening_column + width)
    else:
      if P2630.board[opening_row][opening_column] == 0:
        P2630.counter0 += 1
      else:
        P2630.counter1 += 1

  @staticmethod
  def execute():
    P2630.width = int(reader().rstrip())
    P2630.board = [list(map(int,(reader().rstrip()).split())) for _ in range(P2630.width)]
    P2630.compute_zone(P2630.width,0,0)

    writer(f"{P2630.counter0}\n")
    writer(f"{P2630.counter1}\n")
    # for row in range(P2630.width):
    #   writer(f"{P2630.board[row]}\n")

P2630.execute()