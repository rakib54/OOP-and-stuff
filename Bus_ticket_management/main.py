class Username:
  def __init__(self,username,password):
    self.username = username
    self.password = password

class Bus:
  def __init__(self,coach,driver,arrival,departure,destination,to):
    self.coach = coach
    self.driver = driver
    self.arrival = arrival
    self.departure = departure
    self.destination = destination
    self.to = to
    self.seat = ["Empty" for i in range(20)]

class MyCompany:  # bus install for admin
  total_bus = 5
  total_bus_list = []

  def installed(self):
    bus_no = int(input("Enter a Bus number: "))
    flag = 1
    for bus in self.total_bus_list:
      if bus_no == bus['coach']:
        print("Bus is already installed")
        flag = 0
        break

    if flag:
      bus_driverName = input("Enter the driver name: ")
      bus_arrival = input("Enter Arrival Time: ")
      bus_departure = input("Enter the departure time : ")
      bus_from = input("Enter bus starts from: ")
      bus_to = input("Enter bus destination to: ")
      self.new_bus = Bus(bus_no, bus_driverName, bus_arrival,bus_departure,bus_from,bus_to)
      print("Bus Installed successfully")
      self.total_bus_list.append(vars(self.new_bus))


class BusCounter(MyCompany):
  user_list = []
  bus_seat = 20

  def reservation(self):
    bus_no = int(input("Bus Number: "))
    for bus in self.total_bus_list:
      if bus_no == bus['coach']:
        passenger = input("Passenger Name: ")
        seat_no = int(input("Seat No: "))
        if seat_no - 1 > self.bus_seat:  # index starts with 0 ->0,1,2,3,4...
          print("we have only 20 seats")
        elif bus['seat'][seat_no-1] != "Empty":
          print("Seat already booked")
        else:
          bus['seat'][seat_no - 1] = passenger
      
      else:
        print("No bus available")
        break
    # for bus in self.total_bus_list:
    #   print(bus['seat'])

  def show_bus_info(self):
    pass

company = MyCompany()
customer = BusCounter()

company.installed()
customer.reservation()