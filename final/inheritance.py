# Single Inheritance

class Parent:
    def __init__(self) -> None:
        print("Parent class")
        
class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        print("Child class")

Child()

class Parent:  
    def func_1(self):  
        print ("This function is called from the parent class.")  
  
class Child(Parent):  
    def func_2(self):  
        print ("This function is called from the child class.")  

object = Child()  
object.func_1()  
object.func_2() 

# Multiple Inheritance

class Parent1:
    def __init__(self) -> None:
        print("Parent1 class")

class Parent2:
    def __init__(self) -> None:
        print("Parent2 class")

class Child(Parent1, Parent2):
    def __init__(self) -> None:
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("Child class")

Child()

# Multilevel Inheritance

class Parent:
    def __init__(self) -> None:
        print("Parent class")

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        print("Child class")

class GrandChild(Child):
    def __init__(self) -> None:
        super().__init__()
        print("GrandChild class")

GrandChild()
