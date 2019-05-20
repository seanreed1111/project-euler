'''
004: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def string_is_palindrome(string):
  for index, _ in enumerate(string):
    if string[index] != string[-1-index]:
      return False
  return True


def palindrome(num1, num2):
  product = num1 * num2
  string = str(product)
  return string_is_palindrome(string)


if __name__ == '__main__':
  print("starting")
  # print(91,99,palindrome(91,99))
  # print(11,11,palindrome(11,11))
  results = [i*j for i in range(100,1000)
              for j in range(1000,i, -1)
              if palindrome(i,j) ]
  print(max(results))

