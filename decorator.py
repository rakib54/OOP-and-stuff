import math

def timer(func):
  def inner(*args):
    print("start")
    func(*args)
    print("end")
  return inner

@timer
def fact(n):
  result = math.factorial(n)
  print(f"factorial of {n} is {result}")

# timer(fact)()
fact(10)