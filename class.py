class Phone:
  def __init__(self,name,id,phone):
    self.name = name
    self.id = id
    self.phone = phone

  def call_him(self,number,text):
    talk = f'You are good {text} and your number is {number}'
    return talk


my_phone = Phone('Rakib','17-2','0166')
print(my_phone.call_him('0188', 'Person'))

