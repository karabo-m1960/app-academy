def greet(name):
  print(f"Hello, {name}!")
greet("Alice")

def add(a, b):
  return a + b

results = add(2, 3)
print(results)

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  
def greet(name, greetings="Hello"):
  print(f"{greetings}, {name}!")
  
greet("Bob", "Good morning")