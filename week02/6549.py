import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P6549:
  @staticmethod
  def compute_area(cardin_components, components):
    writer(f"\n{cardin_components} {components}")
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
        P6549.compute_area(cardin_components, received)
    return

P6549.execute()