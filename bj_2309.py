import sys
reader = sys.stdin.readline
writer = sys.stdout.write

nine = 9
dwarfs = [int(reader().rstrip('\n')) for _ in range(nine)]
summation = sum(dwarfs)

def findTwo():
  for index1 in range(nine):
    for index2 in range(index1 + 1, nine):
      if summation - dwarfs[index1] - dwarfs[index2] == 100:
        return [index1, index2]

index1, index2 = findTwo()
dwarfs.pop(index2)
dwarfs.pop(index1)
dwarfs.sort()
writer("\n".join(map(str,dwarfs)))