def percentage(elements):
  sum = 0
  number = elements[0]
  for index in range(1, number+1):
    sum += elements[index]
  average = sum / number
  count = 0
  for index in range(1, number+1):
    if elements[index] > average:
      count += 1
  return round(count/number*100, 3)

number = int(input())
for repetition in range(number):
  print(f"{percentage(list(map(int, input().split()))):.3f}%")

