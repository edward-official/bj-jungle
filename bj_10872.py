input_integer = int(input())
final_answer = 1
for multiplier in range(2, input_integer+1):
  final_answer *= multiplier
print(final_answer)