"""
0 1 2 3 4 5 6 7
1
2
3
4
5
6
7
"""

def is_available(row, column):
  global is_row_occupied, is_increasing_diagonal_occupied, is_decreasing_diagonal_occupied, width
  if is_row_occupied[row]:
    return False
  elif is_increasing_diagonal_occupied[row+column]:
    return False
  elif is_decreasing_diagonal_occupied[row-column+width-1]:
    return False
  else:
    return True
def set_occupation(setting_boolean, row, column):
  global is_row_occupied, is_increasing_diagonal_occupied, is_decreasing_diagonal_occupied, width
  is_row_occupied[row] = setting_boolean
  is_increasing_diagonal_occupied[row+column] = setting_boolean
  is_decreasing_diagonal_occupied[row-column+width-1] = setting_boolean
  return
def nqueen(column):
  global width, count
  if column==width:
    count += 1
    return
  for row in range(width):
    if is_available(row, column):
      set_occupation(True, row, column)
      nqueen(column+1)
      set_occupation(False, row, column)
      
width = int(input())
count = 0
board = [None] * width
is_row_occupied = [False] * width
is_increasing_diagonal_occupied = [False] * (width * 2 - 1) # row+column = 0 ~ 14
is_decreasing_diagonal_occupied = [False] * (width * 2 - 1) # row-column = -7 ~ 7

nqueen(0)
print(count)