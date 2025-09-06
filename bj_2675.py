def ps(repeating_number, target_string):
  final_result = ""
  for letter in target_string:
    final_result += letter * repeating_number
  return final_result

for _ in range(int(input())):
  input_received = input()
  repeating_number = int(input_received.split()[0])
  target_string = input_received.split()[1]
  print(ps(repeating_number, target_string))