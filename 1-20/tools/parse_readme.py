names = ["001: Multiples of 3 and 5",
"002: Even Fibonacci numbers",
"003: Largest prime factor",
"004: Largest palindrome product",
"005: Smallest multiple",
"006: Sum square difference",
"007: 10001st prime",
"008: Largest product in a series",
"009: Special Pythagorean triplet",
"010: Summation of primes"]

def clean(string):
  val = string.lower()
  val = val.replace(":", "")
  val = val.replace(" ","_")
  val = val + ".py"
  return val


filenames = [clean(name) for name in names]
print(filenames)