number1_string, number2_string = input().split()
number1_reversed = int("".join(reversed(number1_string)))
number2_reversed = int("".join(reversed(number2_string)))
print(max(number1_reversed,number2_reversed))