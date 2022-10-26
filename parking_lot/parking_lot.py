class Car:
  def __init__(self,license,model,color):
    self.license = license
    self.model = model
    self.color = color

  # dunder method
  def __repr__(self):
    return f"{self.license}, {self.model}, {self.model}"

class Garage:
  def __init__(self):
    self.car_added = []
    self.spot = 10
    self.car_infos = {}
    self.bill = 0
    self.ticket = []


  def spots_available(self):
    return self.spot

  def add_car_to_garage(self,car):
    
    self.spot_name = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1']
    if self.spots_available() > 0:
      user_data = str(car).split(',')
      self.spot -= 1
      self.car_added.append(user_data)
      self.car_infos = {'Tickets': [], 'License': [], 'Model': [],'Color':[]}
      ticket=""

      for i,val in enumerate(self.car_added):
        ticket += self.spot_name[i] + val[0]      
        self.car_infos['Tickets'].append(ticket)
        self.car_infos['License'].append(val[0])
        self.car_infos['Model'].append(val[1])
        self.car_infos['Color'].append(val[2])
      
      print(f"Successfully Parked and Ticket {ticket}")
    else:
      print("No spots available")

  def un_park(self,ticket,hours):
    past_spot_len = len(self.car_infos['Tickets'])
    if ticket not in self.car_infos['Tickets']: # Complexity O(n) for loop
      print("NO car Found")

    else:
      for i,val in enumerate(self.car_infos['Tickets']):
        if val == ticket:
          print(1)
          print(f"Your license is {self.car_infos['License'][i]}")

          self.car_infos['License'].pop(i)
          self.spot +=1

    if hours > 30:
      print(f"Total Bill: {hours * 5 + 100}")
    else:
      print(f"Total Bill: {hours * 5}")


  def total_cars_in_garage(self):
    for i in self.car_infos.items():
      print(i)

my_garage = Garage()
# user_car = Car('112','Ferrari','Green')
# my_garage.add_car_to_garage(user_car)
# my_garage.un_park('A1112',10)
# my_garage.total_cars_in_garage()

print ('-------------Welcome-------------------')
while True:
  print ('What do you want ?')
  print ('1. Park your car')
  print ('2. Check available space')
  print ('3. Unpark your car')
  print ('4. Exit')

  user_choice = int(input("Enter your Choice: "))
  if user_choice == 1:
    car_license = input("Enter your car license")
    car_model = input("Enter your car Model")
    car_color = input("Enter your car Color")
    user_car = Car(car_license, car_model, car_color) # car class object/instance
    my_garage.add_car_to_garage(user_car)

  if user_choice == 2:
    my_garage.spots_available()

  else:
    break