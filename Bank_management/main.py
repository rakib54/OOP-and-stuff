class Account:
  acc_id  = 1
  def __init__(self,name,nid,age,balance):
    self.name = name
    self.nid = nid
    self.age = age
    self.balance = balance

    # update account acc_id
    self.account_id = Account.acc_id
    Account.acc_id +=1

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount


account1 = Account('Rakib',612243,25,1000)
account1.deposit(2000)
account1.withdraw(1000)

print(account1.balance)