def compute():
  global elements, selected_indexes
  temp = 0
  for index in range(1,len(selected_indexes)):
    temp += abs(elements[selected_indexes[index]] - elements[selected_indexes[index-1]])
  return temp

def select(n):
  global is_element_selected, selected_indexes, final_answer
  if n==number_of_elements:
    temp = compute()
    if final_answer < temp:
      final_answer = temp
    return
  
  for index in range(number_of_elements):
    if not is_element_selected[index]:
      is_element_selected[index] = True
      selected_indexes.append(index)
      select(n+1)
      is_element_selected[index] = False
      selected_indexes.pop()

number_of_elements = int(input())
elements = list(map(int, input().split()))

is_element_selected = [False] * number_of_elements
selected_indexes = []
final_answer = 0
select(0)

print(final_answer)