import sys
sys.setrecursionlimit(1_000_000)
reader = sys.stdin.readline
writer = sys.stdout.write

def is_north_available(row, column):
  global is_point_safe
  if row - 1 < 0:
    return False
  elif not is_point_safe[row-1][column]:
    return False
  return True
def is_south_available(row, column):
  global is_point_safe, width
  if row + 1 >= width:
    return False
  elif not is_point_safe[row+1][column]:
    return False
  return True
def is_west_available(row, column):
  global is_point_safe
  if column - 1 < 0:
    return False
  elif not is_point_safe[row][column-1]:
    return False
  return True
def is_east_available(row, column):
  global is_point_safe, width
  if column + 1 >= width:
    return False
  elif not is_point_safe[row][column+1]:
    return False
  return True

def kill_area(row, column):
  global is_point_safe
  is_point_safe[row][column] = False
  if is_north_available(row,column):
    kill_area(row-1, column)
  if is_south_available(row,column):
    kill_area(row+1, column)
  if is_east_available(row,column):
    kill_area(row, column+1)
  if is_west_available(row,column):
    kill_area(row, column-1)

def count():
  global width, is_point_safe
  temp = 0
  for row in range(width):
    for column in range(width):
      if is_point_safe[row][column]:
        kill_area(row,column)
        temp += 1
  return temp

def drown(height):
  global is_point_safe, width
  is_point_safe = [[True for _ in range(width)] for _ in range(width)]
  for row in range(width):
    for column in range(width):
      if board[row][column] <= height:
        is_point_safe[row][column] = False

def terminal_board():
  global width
  for row in range(width):
    print(board[row])
def terminal_safe():
  global width
  for row in range(width):
    print(is_point_safe[row])

width = int(reader().rstrip())
board = [list(map(int, (reader().rstrip()).split())) for _ in range(width)]
is_point_safe = [[True for _ in range(width)] for _ in range(width)]

final_answer = 1
for height in range(1, 100):
  drown(height)
  temp = count()
  if final_answer < temp:
    final_answer = temp

print(final_answer)