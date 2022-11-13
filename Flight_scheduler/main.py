from TravelAgent import TravelAgent

def main():
  travel_agent = TravelAgent('Rakib')
  trip_info = travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '07-11-2022')
  print('aircraft : ', trip_info.aircraft)
  print('price : ', trip_info.price)
  
  # trip_cities = ['DUB','SYD','LHR','JFK']
  # trip_info2 = travel_agent.set_trip_multi_city_flexible_way(trip_cities, '12-12-2022')
  # print(trip_info2)
  
  
  # for trip in trip_info2[0]:
  #   print(trip)
  
  
if __name__ == '__main__':
  main()