numbers = [6,17,18,104]
#Question:
#for any number n, how do you find the set of factors of n?
#make a dict of prime numbers. Key and value
#make a set of prime numbers and check membership in the set.

# if number is even: #1
#   divide by two,
#   add two to set of factors
#   save the dividend
#   if dividend is even:
#      goto 1
#   if dividend is odd:
  #    goto 2
# else:
  #   goto 2

#if number is odd: #2
#  divide by all primes less than the number
#   if none divide evenly then you are done.
# recusive?







def prime(n): # int :=> bool
  if n == 2: return True
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0: return False
  return True







def find_prime_factors(n): # int :=> [int]

  pass


