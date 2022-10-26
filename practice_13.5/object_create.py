class Calculation:
  count = 0
  def __init__(self):
    self.total_balance = 0
    # type(self).count  += 1
    Calculation.count +=1
    

  def sum(self, a,b):
    self.total_balance+= a + b
    return a + b

  def subtract(self,a,b):
    self.total_balance -= a - b 
    return a - b
    

income = Calculation()
income = Calculation()
income = Calculation()
income = Calculation()
income = Calculation()


print(income.count) # 5 for calling 5 times 

