class RideManager:
  def __init__(self):
    print("Ride manager activated")
    self.__available_car = []
    self.__available_bike= []
    self.__available_cng= []


  def add_vehicle(self, vehicle_type,vehicle):
    
    if(vehicle_type == 'car'):
      self.__available_car.append(vehicle)

    elif(vehicle_type == 'car'):
      self.__available_bike.append(vehicle)

    elif(vehicle_type == 'car'):
      self.__available_cng.append(vehicle)

  def match_a_vehicle(self):
    pass


uber = RideManager()

