import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P6549:
  @staticmethod
  def compute_area():
    return

  @staticmethod
  def execute():
    while True:
      received = list(map(int,(reader().rstrip()).split()))
      if received[0] == 0:
        break
      else:
        cardin_components = received[0]
        received.remove(cardin_components)
        writer(f"{cardin_components} {received}\n")
    return

P6549.execute()