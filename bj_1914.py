def hanoi(tower_from, tower_to, tower_other, n):
  final_count = 0
  if n==1:
    moving_history.append(f"{tower_from} {tower_to}")
    return 1
  
  final_count += hanoi(tower_from, tower_other, tower_to, n-1)
  moving_history.append(f"{tower_from} {tower_to}")
  final_count += 1
  final_count += hanoi(tower_other, tower_to, tower_from, n-1)
  return final_count

moving_history = []
input_integer = int(input())
if input_integer > 20:
  print(2 ** input_integer - 1)
else:
  print(hanoi(1,3,2,input_integer))
  print("\n".join(moving_history))