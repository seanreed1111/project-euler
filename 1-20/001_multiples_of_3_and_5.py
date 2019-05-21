'''
001: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
target = 1000  # up to but not including

def divisible_by_three_or_five(num): #boolean
  return num % 3 == 0 or num % 5 == 0


multiples = [n for n in range(target) if divisible_by_three_or_five(n)]

print(sum(multiples))
# result is the sum of all the multiples
