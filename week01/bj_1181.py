import sys
reader = sys.stdin.readline
writer = sys.stdout.write

def isLeftFirst(object_left, object_right):
  if len(object_left) < len(object_right):
    return True
  elif len(object_left) > len(object_right):
    return False
  if object_left < object_right:
    return True
  elif object_left > object_right:
    return False
  return True
def merge_sort(opening_index, closing_index):
  if opening_index>=closing_index:
    return
  center_index = (opening_index + closing_index) // 2
  merge_sort(opening_index, center_index)
  merge_sort(center_index + 1, closing_index)
  merge(opening_index, closing_index)
  return
def merge(opening_index, closing_index):
  global elements, temp
  center_index = (opening_index + closing_index) // 2
  inserting_index = opening_index
  index1 = opening_index
  index2 = center_index + 1
  while index1<=center_index and index2<=closing_index:
    if isLeftFirst(elements[index1], elements[index2]):
      temp[inserting_index] = elements[index1]
      inserting_index += 1
      index1 += 1
    else:
      temp[inserting_index] = elements[index2]
      inserting_index += 1
      index2 += 1
  while index1 <= center_index:
    temp[inserting_index] = elements[index1]
    inserting_index += 1
    index1 += 1
  while index2 <= closing_index:
    temp[inserting_index] = elements[index2]
    inserting_index += 1
    index2 += 1
  for index in range(opening_index, closing_index+1):
    elements[index] = temp[index]
  return

quantity_of_elements = int(reader())
elements = list(set([reader() for _ in range(quantity_of_elements)]))
quantity_of_elements = len(elements)

temp = [None] * quantity_of_elements
merge_sort(0,quantity_of_elements-1)
writer("".join(map(str, elements)))
