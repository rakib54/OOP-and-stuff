class Vehicle:
    def __init__(self,wheel,price,speed):
        self.wheel = wheel
        self.price = price
        self.speed = speed

class Bus(Vehicle):
    def __init__(self,wheel,price,speed):
        super().__init__(wheel,price,speed)

    def info(self):
        print(self.speed)

# my_bus = Bus('8',10000,120)
# my_bus.info()

# multiple Inheritance

class Grandparent:
  def __init__(self):
    self.string1 = "I am from a grandparent"
        
class Parent(Grandparent):
    def __init__(self):
        self.string1 = "I am from a Parent"
        # super().__init__()
        
    
class Child(Parent,Grandparent):
    def __init__(self):
        self.string1 = "I am from a Child"
        Parent.__init__(self)
        Grandparent.__init__(self)
    
me = Child()
print(me.string1)