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

class Student(School,Teacher):
  def __init__(self,student_name):
    self.student_name = student_name

student = Student('Rakib')
student.say_hello()
    
   


