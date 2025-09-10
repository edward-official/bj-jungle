import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2293:
  record_keys = [] #formation: "{coin_type}+{target_amount}"
  record_values = []

  @staticmethod
  def count_scenario(coin_type, target_amount):
    converted_key = f"{coin_type}+{target_amount}"
    if converted_key in P2293.record_keys:
      found_index = P2293.record_keys.index(converted_key)
      return P2293.record_values[found_index]
    elif target_amount < 0 or not coin_type:
      return 0
    elif target_amount == 0:
      return 1
    answer = P2293.count_scenario(coin_type[1:], target_amount) + P2293.count_scenario(coin_type, target_amount-coin_type[0])
    P2293.record_keys.append(converted_key)
    P2293.record_values.append(answer)
    return answer

  @staticmethod
  def execute():
    cardin_coin_type, target_amount = map(int,(reader().rstrip()).split())
    coin_type = [None] * cardin_coin_type
    for index in range (cardin_coin_type):
      coin_type[index] = int(reader().rstrip())
    final_answer = P2293.count_scenario(coin_type, target_amount)
    writer(f"{final_answer}\n")
    # for index in range(len(P2293.record_keys)):
    #   writer(f"KEY:{P2293.record_keys[index]} > VALUE:{P2293.record_values[index]}\n")
    return
  
P2293.execute()