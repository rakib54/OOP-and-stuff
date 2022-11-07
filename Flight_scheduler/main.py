from TravelAgent import TravelAgent

def main():
  travel_agent = TravelAgent('Rakib')
  trip_info = travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '07-11-2022')
  print('aircraft : ', trip_info.aircraft)
  print('price : ', trip_info.price)
  
  
if __name__ == '__main__':
  main()