import hashlib
from brta import BRTA

license_authority = BRTA()

class User:
  def __init__(self,name,email,password):
    self.name = name
    self.email = email
    self.password = password

    pwd_encrypt = hashlib.md5(password.encode()).hexdigest()

    with open ('urban_riders/user.txt','w') as file:
      file.write(f"{email} {pwd_encrypt}")
    file.close()
    print(f"{self.name} user created successfully")

  @staticmethod
  def log_in(email,password):
    stored_password = ''
    with open('urban_riders/user.txt', 'r') as file:
      lines = file.readlines()
      for line in lines:
          if email in line:
              stored_password = line.split(' ')[1]

    file.close()
    
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    if(stored_password == hashed_password):
      print("valid user")

    else:
      print("invalid user")


class Rider(User):
  def __init__(self,name, email, password,location,balance):
    self.location = location
    self.balance = balance
    super().__init__(name, email, password)

  def set_location(self,location):
    self.location = location

  def get_location(self,location):
    return self.location

  def request_trip(self,destination):
    pass

  def start_trip(self,fair, destination):
    self.balance -= fair


class Driver(User):
  def __init__(self,name, email, password,location,license):
    super().__init__(name, email, password)
    self.location = location
    self.license = license
    self.validDriver = license_authority.validate_license(email, license)
    self.earning = 0

  def take_driving_test(self):
    result = license_authority.driving_test(self.email)
    if result == False:
      print("sorry you have failed")

    else:
      self.license = result
      self.validDriver = result

  def start_trip(self,destination,fair):
    self.earning += fair
    self.location = destination




me = User('rakib', "rakib54@gmail.com", 'hero')
User.log_in("rakib54@gmail.com", 'hero')
shakib = Driver('shakib', 'shakib@gmail.com', 'shakib', 'Brisbane', 1212)

shakib.take_driving_test()
result  = license_authority.validate_license(shakib.email, shakib.license)
print(result)


