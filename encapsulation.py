class Account:
  def __init__(self,name,initial_balance):
    self.name = name
    self.__balance = initial_balance

  def deposit(self,amount):
    print(f'Added {amount} to account')
    self.__balance += amount

  def withdraw(self,amount):
    print(f'Withdraw {amount} from account')
    self.__balance -= amount
  


class StudentAccount(Account):
  def __init__(self,name,initial_balance,age):
    self.age = age
    super().__init__(name,initial_balance)

  @property
  def get_name(self):
     print(self.name)


rakib = StudentAccount('Rakib',50000,25)


rakib.deposit(10000)
rakib.deposit(100000)
rakib.withdraw(40000)

# we can not set balance because its private
# rakib.__balance = -100
print(dir(rakib))

# access private variable
print(rakib._Account__balance)
