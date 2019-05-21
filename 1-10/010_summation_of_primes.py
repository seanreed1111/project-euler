'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt
def prime(n): # int :=> bool
  if n == 2: return True
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0: return False
  return True

def prime_gen():
  n = 2
  while True:
    if prime(n): yield n
    n+=1

if __name__ == '__main__':
  gen = prime_gen()
  sum = 0
  while True:
    prime_num = next(gen)
    if prime_num > 2000000: break
    sum = sum + prime_num
  print(sum)