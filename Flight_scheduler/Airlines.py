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

  def get_air_crafts(self,air_crafts_code):
    return self.air_crafts[air_crafts_code]  
  
  def get_air_crafts_by_distance(self,distance):
    for aircraft in self.air_crafts.values():
      if aircraft.flight_range < distance:
        return aircraft
  
      
Airlines()
      