class Human:
  def __init__(self,name,gender,height,weight):
    self.name = name
    self.gender = gender
    self.height = height
    self.weight = weight

  def get_name(self):
    print(f"Name is {self.name}")

class Engineer(Human):
  def __init__(self,name):
    self.name = name

  # def get_name(self):
  #   print(f"Name was {self.name}")

me = Engineer('Rakib')
me.get_name()