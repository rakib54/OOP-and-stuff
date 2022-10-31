class RideManager:
  def __init__(self):
    print("Ride manager activated")
    self.__income = 0
    self.__trip_history = []
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


  def get_total_income(self):
    # print(self.__income)
    return self.__income

  def trip_history(self):
    return self.__trip_history

  def find_a_vehicle(self, rider,vehicle_type,destination):
    if vehicle_type == 'car':
      if len(self.__available_car) == 0:
        print("No available car")
        return False

      for car in self.__available_car:
        if abs(rider.location-car.driver.location) < 10:
          distance = abs(rider.location - destination)
          fare = distance * car.rate
          if rider.balance < fare:
            print(f"You don't have enough money for this ride: {rider.balance} {fare}")
            return False

          if car.status == 'available':
            car.status = 'unavailable'
            trip_info = f"Match for {rider.name} for fare {fare} with {car.driver.name} from {rider.location} to {destination}"
            rider.start_trip(fare,trip_info)
            car.driver.start_trip(rider.location,destination,fare * 0.8,trip_info)
            self.__income += fare * 0.2
            self.__available_car.remove(car)
            self.__trip_history.append(trip_info)
            print(trip_info)
            return True



uber = RideManager()

