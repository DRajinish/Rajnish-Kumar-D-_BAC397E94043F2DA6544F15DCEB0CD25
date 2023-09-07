def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

result = factorial(3)
print(f"The Factorial of 3 is: {result}")
 