def count(target):
  result = 0
  score = 0
  for index in range(len(target)):
    if target[index] == "O":
      score += 1
      result += score
    else:
      score = 0
  return result

closing_repetition = int(input())
for index in range(closing_repetition):
  print(count(input()))

