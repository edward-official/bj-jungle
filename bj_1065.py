def is_hansu(given_string):
  if int(given_string) <= 0 or len(given_string) == 0:
    return False
  if len(given_string) == 1:
    return True
  digits = [int(letter) for letter in given_string]
  expected_common_difference = digits[1]-digits[0]
  for index in range(1, len(digits)-1):
    if digits[index+1] - digits[index] != expected_common_difference:
      return False
  return True

given_string = input()
count = 0
for target in range(1, int(given_string)+1):
  if is_hansu(str(target)):
    count += 1
print(count)