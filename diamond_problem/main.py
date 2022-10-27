class A:
  def hello(self):
    print("Hello from A")

class B(A):
  def hello(self):
    print("Hello from B")

class C(A):
  def hello(self):
    print("Hello from C")

class D(B,C):  # Searches method in class B first then class C. if it is not found in B and C it searches until the base class
  pass
  # def hello(self):
  #   print("Hello from D")


a = A()
b = B()
c = C()
d = D()

d.hello()