'''
002: Even Fibonacci numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
upper = 4000000 #upper bound
fib_dict = {1:1,2:2}

def even(n):
  return n % 2 == 0

def fib(n):
  #defined for n>=1
  if n <= 0: assert False
  if n == 1: return 1

  if fib_dict.get(n) is not None:
    return fib_dict.get(n)
  else:
    fib_dict[n] = fib(n-1) + fib(n-2)
  return fib_dict[n]

print(fib(100))


