import sys
reader = sys.stdin.readline
writer = sys.stdout.write
number_of_elements = int(reader())
elements = [int(reader()) for _ in range(number_of_elements)]
elements.sort()
writer("\n".join(map(str, elements)))