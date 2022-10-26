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

my_bus = Bus('8',10000,120)
my_bus.info()