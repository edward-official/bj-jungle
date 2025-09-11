import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2293:
  @staticmethod
  def count_scenario(coin_type, target_amount):
    records = [0] * (target_amount + 1)
    records[0] = 1
    coin_type.sort()
    for coin in coin_type:
      for amount in range(coin, target_amount+1):
        records[amount] += records[amount-coin]
    return records[target_amount]

  @staticmethod
  def execute():
    cardin_coin_type, target_amount = map(int,(reader().rstrip()).split())
    coin_type = [int(reader().rstrip()) for _ in range(cardin_coin_type)]
    answer = P2293.count_scenario(coin_type, target_amount)
    writer(f"{answer}\n")
    return
  
P2293.execute()