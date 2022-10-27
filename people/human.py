class Human:
  def __init__(self,name,gender,height,weight):
    self.name = name
    self.gender = gender
    self.height = height
    self.weight = weight

class CseEngineer(Human):
  def __init__(self,name,gender,height,weight,position,love_to_code):
    self.position = position
    self.love_to_code = love_to_code
    super().__init__(name,gender,height,weight)

class Police(Human):
  def __init__(self,name,gender,height,weight,nationality,nid):
    self.nationality = nationality
    self.nid = nid
    super().__init__(name,gender,height,weight)

  def Nationality(self):
    print(f"Nationality is {self.nationality}")


me = CseEngineer('Tamim','Male',65,70,"Software Engineer",True)
# print(me.love_to_code)
# print(me.gender)

# we can set value by parameter name. so we don't have to maintain order
eng = CseEngineer(position="Software Engineer", love_to_code = True, name=True,gender='male',height=70,weight=52,)
print(eng.name) 

police = Police('Rafiq','Male',65,70,'Bangladeshi',True)
police.Nationality()