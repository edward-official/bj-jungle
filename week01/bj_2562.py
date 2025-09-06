import math

closing = 9
find_value = -math.inf
find_index = -1
for index in range(1, closing+1):
  value = int(input())
  if value > find_value:
    find_value = value
    find_index = index

print(find_value)
print(find_index)
