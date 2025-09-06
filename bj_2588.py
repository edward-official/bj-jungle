number1 = int(input())
number2_string = input()

for index in range(2,-1,-1):
  digit = int(number2_string[index])
  print(number1 * digit)

print(number1 * int(number2_string))