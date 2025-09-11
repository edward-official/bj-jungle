import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P9012:
  @staticmethod
  def execute():
    cardin_readings = int(reader().rstrip())
    for _ in range(cardin_readings):
      reading = reader().rstrip()
      counting = 0
      is_valid = True
      for letter in reading:
        if letter == "(":
          counting += 1
        else:
          counting -= 1
          if counting < 0:
            is_valid = False
            break
      if is_valid and counting == 0:
        writer("YES\n")
      else:
        writer("NO\n")
    return

P9012.execute()