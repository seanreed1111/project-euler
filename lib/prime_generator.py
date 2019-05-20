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