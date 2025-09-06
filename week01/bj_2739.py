def times_table(n):
  for multiplier in range(1,10):
    print(f"{n} * {multiplier} = {n * multiplier}")

n = int(input())
times_table(n)