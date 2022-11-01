class School:
  def __init__(self,name):
    self.school_name = name

  def say_hello(self):
    print("Hello from school")

class Teacher:
  def __init__(self,teacher_name):
    self.teacher_name = teacher_name

  def say_hello(self):
    print("Hello from Teacher")

class Student:
  def __init__(self,student_name,obj):
    self.student_name = student_name
    
    # duck type directly called method under given obj
    obj.say_hello()

school = School("BF Shahin College")
teacher = Teacher("Rafiqul Islam")

student = Student('Rakib',school)
student = Student('Rakib',teacher)

""" 
Duck Typing is a term commonly related to dynamically typed programming languages and polymorphism. The idea behind this principle is that the code itself does not care about whether an object is a duck, but instead it does only care about whether it quacks.
"""
