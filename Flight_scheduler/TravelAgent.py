from AllAirport import AllAirport
from Airlines import Airlines

class TravelAgent:
  def __init__(self,name):
    self.name = name
    self.trips = None
    self.all_airports = AllAirport()
    self.all_airlines = Airlines() 
    
  """
  params: 
  start: staring city code
  end: destination
  start_date: when you want to start your journey
  
  return ticket price, aircraft
  """
    
  def set_trip_one_city_one_way(self,start,end,start_date):
    price = self.all_airports.get_ticket_price(start, end)
    distance = self.all_airports.distance_between_two_airports(start, end)
    aircraft = self.all_airlines.get_air_crafts_by_distance(distance)
    
    return price,distance
  
  def set_trip_one_city_two_way(self):
    pass
  
  def set_trip_multiple_city_one_way(self):
    pass
  
  def set_trip_multiple_city_round(self):
    pass