class Person:
  def __init__(self,name,age,phone):
    assert age > 13, f"age must be up greater than 13"
    assert len(phone) == 11, "Invalid phone number"
    self.name = name
    self.age = age
    self.phone = phone

  def __repr__(self): 
    return f"{self.name} {self.age} {self.phone}"

user = Person('Rak', 14, "0199211212")
print(user)
