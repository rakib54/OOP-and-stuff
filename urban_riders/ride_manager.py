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

  def get_available_cars(self):
    return self.__available_cars

  def find_a_vehicle(self, rider,vehicle_type,destination):
    if vehicle_type == 'car':
      if len(self.__available_car) == 0:
        print("No available car")
        return False

      for car in self.__available_car:
        # print("Potential ", rider.location,car.driver.location)
        if abs(rider.location-car.driver.location) < 10:
          if car.status == 'available':
            car.status = 'unavailable'
            print(len(self.__available_car))
            self.__available_car.remove(car)
            print(len(self.__available_car))
            print("Find a matching for you")
            return True



uber = RideManager()

