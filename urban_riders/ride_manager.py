class RideManager:
  def __init__(self):
    print("Ride manager activated")
    self.__income = 0
    self.__trip_history = []
    self.__available_vehicle = []
    self.__available_bike= []
    self.__available_cng= []


  def add_vehicle(self, vehicle_type,vehicle):
    
    if(vehicle_type == 'vehicle'):
      self.__available_vehicle.append(vehicle)

    elif(vehicle_type == 'bike'):
      self.__available_bike.append(vehicle)

    elif(vehicle_type == 'cng'):
      self.__available_cng.append(vehicle)

  def get_available_vehicles(self):
    return self.__available_vehicles


  def get_total_income(self):
    # print(self.__income)
    return self.__income

  def trip_history(self):
    return self.__trip_history

  def find_a_vehicle(self, rider,vehicle_type,destination):
    if vehicle_type == 'vehicle':
      vehicles = self.__available_vehicle
    elif vehicle_type == 'bike':
      vehicles = self.__available_bike
    else:
      vehicles = self.__available_cng
    

    if len(vehicles) == 0:
        print("No available vehicles")
        return False

    for vehicle in vehicles:
      if abs(rider.location-vehicle.driver.location) < 10:
        distance = abs(rider.location - destination)
        fare = distance * vehicle.rate
        if rider.balance < fare:
          print(f"You don't have enough money for this ride: {rider.balance} {fare}")
          return False

        if vehicle.status == 'available':
          vehicle.status = 'unavailable'
          trip_info = f"Match for {rider.name} for fare {fare} with {vehicle.driver.name} from {rider.location} to {destination}"
          rider.start_trip(fare,trip_info)
          vehicle.driver.start_trip(rider.location,destination,fare * 0.8,trip_info)
          self.__income += fare * 0.2
          vehicles.remove(vehicle)
          self.__trip_history.append(trip_info)
          print(trip_info)
          return True



uber = RideManager()

