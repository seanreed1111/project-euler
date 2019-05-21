'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

counter = 0
target_len = 10001

gen = prime_gen()
while counter < target_len:
  counter += 1
  num = next(gen)
print(counter, num)


