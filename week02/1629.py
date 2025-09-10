import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P1629:
  # base / divider == quotient ... remainder
  # base == divider * quotient + remainder
  @staticmethod
  def compute(base, exponent, divider):
    if exponent == 1:
      return base % divider
    
    exponent_halfed = exponent // 2
    if exponent % 2 == 0:
      temp = P1629.compute(base, exponent_halfed, divider)
      return (temp * temp) % divider
    else:
      temp1 = P1629.compute(base, exponent_halfed, divider)
      temp2 = (temp1 * base) % divider
      return (temp1 * temp2) % divider

  @staticmethod
  def execute():
    # 10 11 12
    base, exponent, divider = map(int,(reader().rstrip()).split())
    final_answer = P1629.compute(base, exponent, divider)
    writer(f"{final_answer}\n")
    return
  
P1629.execute()