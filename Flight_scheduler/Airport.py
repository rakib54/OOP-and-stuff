class Airport:
  def __init__(self,name,country,lat,long,rate):
    self.name = name
    self.country = country
    self.lat = lat
    self.long = long
    self.rate = rate

  def __repr__(self):
    return f"Airport: {self.name} in {self.country} latency: {self.lat} long: {self.long} rate: {self.rate}"