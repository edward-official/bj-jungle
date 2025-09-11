import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P17608:
  @staticmethod
  def execute():
    cardin_pillars = int(reader().rstrip())
    pillars = []
    for _ in range(cardin_pillars):
      pillars.append(int(reader().rstrip()))
    
    recent_tallest = 0
    answer = 0
    for index in range(cardin_pillars-1, -1, -1):
      current_pillar = pillars[index]
      if recent_tallest < current_pillar:
        recent_tallest = current_pillar
        answer += 1
    writer(f"{answer}\n")
    return

P17608.execute()