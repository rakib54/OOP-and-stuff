class Trip:
  def __init__(self,trip_cities,aircraft,price, start_date,route=' '):
    self.trip_cities = trip_cities
    self.start_date = start_date
    self.aircraft = aircraft
    self.trip_route = route
    self.price = price
    
  def __repr__(self):
    return f"AirCraft: {self.aircraft} trip_cities: {self.trip_cities} start_date: {self.start_date} trip_route: {self.trip_route} cost: {self.price}"
    