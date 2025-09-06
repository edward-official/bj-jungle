def sum(integer_value):
  if integer_value == 0:
    return 0
  else:
    return sum(integer_value - 1) + integer_value
  
print(sum(5))