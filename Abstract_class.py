from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def make_sound(self):
    print("Meow Meow")

  @abstractmethod
  def name(self):
    print("My name is cat")


class Dog(Animal):
  def __init__(self):
    pass
    # need to override 
  def make_sound(self):
    print("HugHug")


dog = Dog()

dog.make_sound()
dog.name()
