def sieve(max_value):
  is_prime = [True] * (max_value + 1)
  is_prime[0] = False
  is_prime[1] = False
  square_root = int(max_value ** 0.5)
  for prime_candidate in range(2, square_root + 1):
    if is_prime[prime_candidate]:
      first_composite = prime_candidate * prime_candidate
      for composite in range(first_composite, max_value + 1, prime_candidate):
        is_prime[composite] = False
  return is_prime

def goldbach(even_number, is_prime):
  if even_number == 4:
    return 2, 2
  element1 = 0
  element2 = 0
  for element in range(3, even_number // 2+1):
    if is_prime[element] and is_prime[even_number-element]:
      element1 = element
      element2 = even_number-element
  return element1, element2

number_repetition = int(input())
prime_table = sieve(10000)

for _ in range(number_repetition):
  n = int(input())
  element1, element2 = goldbach(n, prime_table)
  print(element1, element2)
