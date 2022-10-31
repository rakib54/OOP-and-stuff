import hashlib
import random
from brta import BRTA
from vehicles import Car,Bike,Cng
from ride_manager import uber

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
      self.validDriver = True

  def register_vehicle(self,vehicle_type,license_plate,rate):
    if self.validDriver is True:
      if vehicle_type == 'car':
        new_vehicle = Car(vehicle_type, license_plate, rate,self)
        uber.add_vehicle(vehicle_type,new_vehicle)

      elif vehicle_type == 'bike':
        new_vehicle = Bike(vehicle_type, license_plate, rate,self)
        uber.add_vehicle(vehicle_type, new_vehicle)

      else:
        new_vehicle = Cng(vehicle_type, license_plate, rate, self)
        uber.add_vehicle(vehicle_type,new_vehicle)

    else:
      print("You are not a valid driver")

  def start_trip(self,destination,fair):
    self.earning += fair
    self.location = destination


rider1 = Rider('Rakib','rakibur54@gmail.com','rider1',random.randint(0,30),5000)

driver1 = Driver('Driver1','driver1@gmail.com','driver1',random.randint(0,30),5000)
driver1.take_driving_test()
driver1.register_vehicle('car', 1200, 500)


driver2 = Driver('Driver2','driver2@gmail.com','driver1',random.randint(0,30),5000)
driver2.take_driving_test()
driver2.register_vehicle('car', 1200, 500)
driver3 = Driver('Driver3','driver3@gmail.com','driver1',random.randint(0,30),5000)
driver3.take_driving_test()
driver3.register_vehicle('car', 1200, 500)


uber.find_a_vehicle(rider1, 'car', 90)


