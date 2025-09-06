def recursive_z(opening_row, opening_column, width, accumulating_value):
  global target_row, target_column
  half_width = width // 2
  half_square = half_width ** 2
  if width == 0:
    return accumulating_value
  elif target_row < opening_row + half_width and target_column < opening_column + half_width:
    return recursive_z(opening_row, opening_column, half_width, accumulating_value)
  elif target_row < opening_row + half_width and opening_column + half_width <= target_column:
    return recursive_z(opening_row, opening_column + half_width, half_width, accumulating_value + half_square)
  elif opening_row + half_width <= target_row and target_column < opening_column + half_width:
    return recursive_z(opening_row + half_width, opening_column, half_width, accumulating_value + half_square * 2)
  elif opening_row + half_width <= target_row and opening_column + half_width <= target_column:
    return recursive_z(opening_row + half_width, opening_column + half_width, half_width, accumulating_value + half_square * 3)
  return

width, target_row, target_column = map(int, input().split())
width = 2 ** width
print(recursive_z(0,0,width,0))