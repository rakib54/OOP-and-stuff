import csv
from Airport import Airport

class AllAirport:
  def __init__(self):
    self.airports = None
    self.load_airport_data('Flight_scheduler/data/airport.csv')
  
  def load_airport_data(self,file_path):
    airports = {}
    currency_rates = {}
    country_currency = {}
    
    # get_currency_name <-----> rate
    with open('Flight_scheduler/data/currencyrates.csv','r') as file:
      lines = csv.reader(file)
      for line in lines:
        currency_rates[line[1]] = line[2]   
    file.close()
    
    
    # country <-----> currency name
    with open('Flight_scheduler/data/countrycurrency.csv','r') as file:
      lines = csv.reader(file)
      for line in lines:
        country_currency[line[0]] = line[1]
    file.close()
    
    # create airport
    
    with open(file_path,'r',encoding="utf8") as file:
      lines = csv.reader(file)
      try:
        for line in lines:
          country = line[3]
          currency = country_currency[country]
          rate = currency_rates[currency]
          airports[line[4]] = Airport(line[4],line[1],line[2],line[3],line[6],line[7],rate)
      except KeyError as k:
        print(k)
        
    file.close()
        
    self.airports = airports
    
    for airport in airports.items():
      print(airport)
    
AllAirport()