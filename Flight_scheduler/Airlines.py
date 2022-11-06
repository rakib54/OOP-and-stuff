import csv
from Aircraft import Aircraft

class Airlines:
  def __init__(self):
    self.air_crafts = None
    self.load_aircraft_data('Flight_scheduler/data/aircraft.csv')
    
  def load_aircraft_data(self,csv_file):
    air_crafts = {}
    
    with open(csv_file, 'r') as file:
      lines = csv.reader(file)
      next(lines) # skip first row
      for line in lines:
        air_crafts[line[0]] = Aircraft(line[3],line[0],line[1],line[4])
    file.close()
    
    self.air_crafts = air_crafts
    
    # for air in air_crafts.items():
    #   print(air)

  def get_air_crafts(self,code):
    return self.air_crafts[code]  
  
      
Airlines()
      