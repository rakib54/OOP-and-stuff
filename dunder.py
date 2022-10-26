class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    def __add__(self, other):
       return self.money + other.money

    def __call__(self):
      print(f'{self.name} has {self.money} Taka')

tom = Person('Tom',24,1500)
jerry = Person('jerry',24,1000)
print(tom + jerry)

tom()
jerry()

