class Item:
  all=[]
  def __init__(self,itemName,itemPrice):
    self.__itemName = itemName
    self.__itemPrice = itemPrice
    self.all.append(self)

  def __repr__(self):
    return f"Item({self.__itemName}  {self.__itemPrice})"

item1 = Item('Pepsi', 25)
item2 = Item('pen', 10)

# add private item to its class
item1._Item__discount = 10
item2.offer = "60% Off"

# access private attributes 
print(item1._Item__itemName)
# print(Item.all)
print(item1.__dict__)