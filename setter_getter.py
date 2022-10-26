class Student:
  def __init__(self):
    self._name = 'Rasel'

  @property
  def get_name(self):
    print("I am getter")
    return self._name

# must set the property decorator in the getter function
  @get_name.setter
  def set_name(self,name):
    self._name = name

  def del_name(self):
    del self._name


class Me(Student):
  def __init__(self):
    super().__init__()

m = Me()
print(m.get_name)
m.set_name = 'Tami'
print(m.get_name)
print(m.__dir__())
m.del_name()

# print(m.__dir__())


    