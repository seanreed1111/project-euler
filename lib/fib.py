from functools import lru_cache

@lru_cache(maxsize=1010)
def fib_cached(n):
  if n == 1: return 1
  if n == 2: return 1

  return fib_cached(n-1) + fib_cached(n-2)

fib_dict = {1:1,2:2}
def fib(n):
  #defined for n>=1
  if n <= 0: assert False
  if n == 1: return 1

  if fib_dict.get(n) is not None:
    return fib_dict.get(n)
  else:
    fib_dict[n] = fib(n-1) + fib(n-2)
  return fib_dict[n]

#@lru_cache(maxsize=2048)
def fib_iterative(n):
  #1,1,2,3,5,8,13,21,34,55,...
  if n == 1: return 1
  if n == 2: return 1
  a,b = 1,1
  for i in range(2,n):
    a,b = b, b+a
  return b


if __name__ == '__main__':
  for i in range(1,5000):
    num = fib_iterative(i)
    print(i,len(str(num)))

