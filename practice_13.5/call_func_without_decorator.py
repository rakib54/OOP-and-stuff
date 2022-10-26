# class Animal:
#   def leg(self,name,no_of_legs):
#     self.legs = no_of_legs
#     self.name = name
#     print(f"{self.name} has {self.legs} legs")


# dog = Animal()
# dog.leg('Dog', 4)

@decorator_showname
def hypotenuse2(a, b):
    return round(float((a*a) + (b*b))**0.5, 2)

hypotenuse2(1,2)