class Trip:
  def __init__(self,trip_cities, start_date):
    self.trip_cities = trip_cities
    self.start_date = start_date
    self.aircraft = None
    self.trip_route = None
    self.cost = None
    
  def __repr__(self):
    return f"AirCraft: {self.aircraft} trip_cities: {self.trip_cities} start_date: {self.start_date} trip_route: {self.trip_route} cost: {self.cost}"
    