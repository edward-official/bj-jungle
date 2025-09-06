number1 = int(input())
number2 = int(input())
number3 = int(input())
result = number1 * number2 * number3
counts = [0] * 10

result_string = str(result)
for index in range(len(result_string)):
  digit = int(result_string[index])
  counts[digit] += 1

for index in range(len(counts)):
  print(counts[index])