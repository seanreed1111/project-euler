'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000.
Find the product abc.
'''
from math import sqrt
target_sum = 1000
for c in range(target_sum):
  for b in range(target_sum - c,1,-1):
    for a in range(target_sum - c - b,1,-1):
      if (a + b + c == 1000) and (a*b*c != 0) and (a**2 + b**2 - c**2)==0:
        print("a,b,c",a,b,c)
        print("a*b*c",a*b*c)
        print("a^2 + b^2 - c^2",a**2 + b**2 - c**2)
        raise StopIteration("Problem solution found.")