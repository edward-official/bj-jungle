import re
import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P10000:
  @staticmethod
  def execute():
    x_opening = []
    x_closing = []
    cardin_circles = int(reader().rstrip())
    for _ in range(cardin_circles):
      x_center, radius = map(int, (reader().rstrip()).split())
      x_opening.append(x_center-radius)
      x_closing.append(x_center+radius)
    return

P10000.execute()
