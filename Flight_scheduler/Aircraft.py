class Aircraft:
    def __init__(self, make, code, typ, flight_range):
        self.make = make
        self.code = code
        self.typ = typ
        self.flight_range = flight_range
        
    def get_make(self):
      return self.make
    
    def get_flight_range(self):
      return self.flight_range

    def __repr__(self):
        return f"AirCraft make: {self.make} code: {self.code} typ: {self.typ} range: {self.flight_range}"
