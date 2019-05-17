numbers = [6,17,18,104]
def prime(n): # int :=> bool
  if n == 2: return True
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0: return False
  return True

#Question:
#for any number n, how do you find the set of factors of n?
#make a dict of prime numbers. Key and value
# key is the number, value is the exponent, ie how many times the number divides evenly, e.g. prime factors of 40 = {2:3, 5:1}
#make a set of prime numbers and check membership in the set.

# if number is even: #1
#   divide by two,
#   increment two as a factor
#   save the dividend. This is the new number
#   if dividend is 1 then you are DONE.
#   if dividend is even:
#      goto 1
#   if dividend is odd:
#      goto 2
# else:
#   goto 2

#if number is odd: #2
#    divide by 3 and check for remainder == 0
#    if remainder == 0
#      save the dividend. This is the new number
#      add three to the set of factors
#
#  divide by all primes less than the number
#   if none divide evenly then you are done.
# recusive?
#
#
#
#
#
#
#











