import sys
reader = sys.stdin.readline
writer = sys.stdout.write
elements_quantitiy = int(reader())
radix_array = [0] * 10001
for _ in range(elements_quantitiy):
  radix_array[int(reader())] += 1

for radix in range(10001):
  for _ in range(radix_array[radix]):
    writer(f"{radix}\n")