'''
005: Smallest multiple
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
'''

#prime factors of 2520 are {2: 3, 3: 2, 5: 1, 7: 1}

#would expect prime factors of the desired answer are:
#{2: 4, 3: 2, 5: 1, 7: 1, 11:1,13:1,17:1,19:1}

#1 find prime factorization of all numbers from 1 to 20
#2 use the max of each key and combine into new counter
#multiply all keys by their values

from math import sqrt
from collections import Counter, defaultdict

def find_factors(n): # int :=> [int]
  factors = Counter()
  #check even numbers
  while (n % 2 == 0):
    factors.update([2])
    n = n // 2

  for i in range(3,n+1,2):
    while (n % i == 0):
      factors.update([i])
      n = n // i

  return factors

if __name__ == '__main__':
  all_factors = [find_factors(i) for i in range(2,21)]
  flattened_factors = [(key,factor[key])
                      for factor in all_factors
                      for key in factor.keys()
                      ]

  d = defaultdict(list)
  for k, v in flattened_factors:
    d[k].append(v)


  factor_dict = {k:max(d[k]) for k in d}

  # #now do the sumproduct. could also do reduce
  ans = 1
  for key in factor_dict:
    ans = ans* (key**factor_dict[key])
  print(ans)
