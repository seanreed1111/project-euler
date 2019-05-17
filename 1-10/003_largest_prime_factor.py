'''
003: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''
from math import sqrt
#target = 600851475143
target = 98
# factors = find_prime_factors(target)

# answer = max(factors)


def prime(n): # int :=> bool
  if n == 2: return True
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0: return False
  return True
