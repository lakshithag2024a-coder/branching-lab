# adding comment on github browser(online)
# calculator.py
# A simple calculator program
def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  if b == 0:
    return "Cannot divide by zero"
  return a / b

if __name__ == "__main__":
 x = 10
 y = 5
 print("Sum:", add(x, y))
 print("Difference:", subtract(x, y))
