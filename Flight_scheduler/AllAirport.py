import csv

class AllAirport:
  def __init__(self):
    self.load_airport_data('Flight_scheduler/data/currencyrates.csv')
  
  def load_airport_data(self,file_path):
    with open(file_path,'r') as file:
      lines = csv.reader(file)
      for line in lines:
        print(line)
    
AllAirport()