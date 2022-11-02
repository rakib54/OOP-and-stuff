class User:
  user_lst = [] # class variable
  def __init__(self, username, password):
    self.username = username # instance variable
    self.password = password

class Item:
  def __init__(self,ItemID,price,description,quantity):
    self.ItemID = ItemID
    self.price = price
    self.description = description
    self.quantity = quantity

class ShoppingBasket:
  user_lst =[]  # [{"name":"raki","password":"123"},{"name":"tam","password":"1233"]
  user_ordered_data = {}
  itemDB = []

  def get_userList(self):
    for user in self.user_lst:
      print(user['name'])
    return self.user_lst

  def create_account(self):
    name = input("Enter your username: ")
    isNameExist = False
    for user in self.get_userList():
      if user.username == name:
        print("Account already exists")
        isNameExist = True
        break
    if isNameExist == False:
      password = input("Enter your password: ")
      self.new_user = User(name, password)
      self.user_lst.append({"name":name, "password":password})
      print("Account created successfully")

    def addItemToCart(self,username):
      if username in self.user_ordered_data.keys():
        itemId = input("Enter Item Id: ")
        quantity = int(input("Enter item quantity: "))

        flag = 0
        for i in self.itemDB:
          if i['itemId'] == itemId and i['quantity'] >= quantity:
            print("items available")
            flag = 1
            break

        if not flag:
          print("items not available")
        else:
          self.user_ordered_data[username] = [{"itemID":itemId, "quantity":quantity}]

    def updateProductCart(self,username):
      username = input("Enter your name: ")
      itemId = input("Enter your ItemId: ")
      quantity = int(input("Enter your updated quantity: "))
      
      for i in self.user_ordered_data[username]:
        if i['itemID'] == itemId:
          if quantity <= i['quantity']:
            i['quantity'] = quantity
          else:
            print("out of stock")
            break

    def deleteProductCart(self):
        flag = 0
        for i in self.itemDB:
          if i['itemId'] == itemId and i['quantity'] <= quantity:
            print("items available")
            flag = 1
            break

        if flag:
          for i in self.user_ordered_data[username]:
            if(i['itemID'] == itemId):
              self.user_ordered_data[username].remove(i)




b = ShoppingBasket()
b.create_account()
print(b.get_userList())





# a = {"rakib":[{"itemID":12,"price":200}]}
# a['rakib'].append({"item":13})

# for i in a['rakib']:
#   if(i['itemID'] == 12):
#     a['rakib'].remove(i)
# print(a['rakib'])