import sys
sys.setrecursionlimit(10**8)
reader = sys.stdin.readline
writer = sys.stdout.write

class P10830:
  width = None
  record_key = []
  record_value = []

  @staticmethod
  def product(matrix1, matrix2):
    temp_matrix = []
    for row in range(P10830.width):
      temp_row = []
      for column in range(P10830.width):
        temp_component = 0
        for offset in range(P10830.width):
          temp_component += matrix1[row][offset] * matrix2[offset][column]
          temp_component %= 1000
        temp_row.append(temp_component)
      temp_matrix.append(temp_row)
    return temp_matrix
  
  @staticmethod
  def compute_power(matrix, exponent):
    compound_key = f"{matrix}+{exponent}"
    # writer(f"\ncompute method called: {exponent}")
    if compound_key in P10830.record_key:
      target_index = P10830.record_key.index(compound_key)
      # writer(f"\n[{exponent}]: used record ✅")
      return P10830.record_value[target_index]
    elif exponent == 1:
      # writer(f"\n[{exponent}]: itself")
      return matrix
    
    halfed_exponent = exponent // 2
    if exponent % 2 == 0:
      computed_halfed = P10830.compute_power(matrix,halfed_exponent)
      computed = P10830.product(computed_halfed, computed_halfed)
      P10830.record_key.append(compound_key)
      P10830.record_value.append(computed)
      # writer(f"\n[{exponent}]: computed")
      return computed
    else:
      computed = P10830.product(P10830.compute_power(matrix,halfed_exponent), P10830.compute_power(matrix,halfed_exponent+1))
      P10830.record_key.append(compound_key)
      P10830.record_value.append(computed)
      # writer(f"\n[{exponent}]: computed")
      return computed
  
  @staticmethod
  def execute():
    P10830.width, exponent = map(int,(reader().rstrip()).split())
    matrix = [list(map(int,(reader().rstrip()).split())) for _ in range(P10830.width)]
    answer = P10830.compute_power(matrix, exponent)
    for row in range(P10830.width):
      for column in range(P10830.width):
        writer(f"{answer[row][column]%1000} ")
      writer(f"\n")
    return

P10830.execute()