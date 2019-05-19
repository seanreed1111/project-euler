from math import sqrt
def prime(n): # int :=> bool
  if n == 2: return True
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0: return False
  return True

if __name__ == '__main__':
  numbers = [6,17,18,104]
  for i in numbers:
    print(i, prime(i))

