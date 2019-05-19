'''
003: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''
from math import sqrt
from collections import Counter
# def prime(n): # int :=> bool
#   if n == 2: return True
#   for i in range(2, int(sqrt(n)) + 1):
#     if n % i == 0: return False
#   return True

def find_factors(n): # int :=> [int]
  factors = Counter({2:0})
  #check even numbers
  while (n % 2 == 0):
    factors.update([2])
    n = n // 2

  for i in range(3,int(sqrt(n))+1,2):
    while (n % i == 0):
      factors.update([i])
      n = n // i

  return factors

if __name__ == '__main__':

#  target = 256
#  target = 1280
#  target = 3604957440
  target = 600851475143
  factors = find_factors(target)
  print(max(factors))


