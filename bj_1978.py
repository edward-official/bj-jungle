def is_prime(number):
  if number < 2:
    return False
  elif number == 2:
    return True
  elif number % 2 == 0:
    return False
  for divier in range (3, int(number ** 0.5) + 1, 2):
    if number % divier == 0:
      return False
  return True

closing_repetition = int(input())
count_prime = 0
elements = map(int, input().split())
for element in elements:
  if is_prime(element):
    count_prime += 1

print(count_prime)