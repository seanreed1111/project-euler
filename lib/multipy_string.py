def multiply_string(string,num_of_digits=13):
  product = 1
  for i in range(num_of_digits):
    product = product * int(string[i])
  return product