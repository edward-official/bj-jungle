import sys, math
reader = sys.stdin.readline
writer = sys.stdout.write

def compute():
  global number_of_cities, selected_cities
  temp = 0
  for index in range(0,number_of_cities):
    city_from = selected_cities[index]
    city_to = selected_cities[index+1]
    if prices[city_from][city_to] == 0:
      return math.inf
    else:
      temp += prices[city_from][city_to]
  return temp

def select(n):
  global number_of_cities, final_answer, is_city_selected, selected_cities
  if n==number_of_cities:
    selected_cities.append(selected_cities[0])
    temp = compute()
    selected_cities.pop()
    if temp < final_answer:
      final_answer = temp
    return
  for city in range(number_of_cities):
    if not is_city_selected[city]:
      is_city_selected[city] = True
      selected_cities.append(city)
      select(n+1)
      is_city_selected[city] = False
      selected_cities.pop()

number_of_cities = int(reader().rstrip("\n"))
prices = [list(map(int, (reader().rstrip("\n")).split())) for _ in range(number_of_cities)]

selected_cities = []
is_city_selected = [False] * number_of_cities
final_answer = math.inf
select(0)
print(final_answer)