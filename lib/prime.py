def prime(n): # int :=> bool
  if n == 2: return True
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0: return False
  return True

if __name__ == '__main__':
  primes = [3433,  3449,  3457,  3461,  3463,  3467,  3469,  3491,  3499,  3511]

  print(all([prime(n) for n in primes])) # True