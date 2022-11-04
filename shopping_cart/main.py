class User:
  user_lst = [] # class variable
  def __init__(self, username, password):
    self.username = username # instance variable
    self.password = password

class Item:
  def __init__(self,ItemId,price,description,quantity):
    self.ItemId = ItemId
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
      self.user_lst.append({"username":name, "password":password})
      print("Account created successfully")


  def addItemToDatabase(self): # admin create product
      itemId = input("Enter your product id: ")
      description = input("Enter your product name: ")
      price = int(input("Enter your price: "))
      quantity = int(input("Enter your quantity: "))

      self.newItem = Item(itemId, price, description, quantity)
      self.itemDB.append(vars(self.newItem))


  def addItemToCart(self,username):
      itemId = input("Enter Item Id: ")
      quantity = int(input("Enter item quantity: "))

      flag = 0
      for i in self.itemDB:
        if i['ItemId'] == itemId and i['quantity'] >= quantity:
          print("items available")
          flag = 1
          break

      if not flag:
        print("items not available")
      else:
        self.user_ordered_data[username] = [{"ItemId":itemId, "quantity":quantity}]

  def updateProductCart(self,username):
      itemId = input("Enter your ItemId: ")
      quantity = int(input("Enter your updated quantity: "))
      
      for i in self.user_ordered_data[username]:
        if i['ItemId'] == itemId:
          if quantity <= i['quantity']:
            i['quantity'] = quantity
          else:
            print("out of stock")
            break

  def deleteProductCart(self,username,itemId):
        flag = 0
        for i in self.itemDB:
          if i['ItemId'] == itemId:
            flag = 1
            break

        if flag: # item available
          for i in self.user_ordered_data[username]:
            if(i['ItemId'] == itemId):
              self.user_ordered_data[username].remove(i)

  def showDatabase(self):
      print(self.itemDB)
      print(self.user_ordered_data)
      print(self.user_lst)

basket = ShoppingBasket()
basket.addItemToDatabase()
basket.showDatabase()

while True:
  print("1. Create an Account\n2. Login to your account\n3. Exit")
  choice = int(input("Enter your choice: "))
  basket = ShoppingBasket()
  if choice == 3:
    break
  elif choice == 1:
    basket.create_account()
  elif choice == 2:
    name = input("Enter Your Name: ")
    password = input("Enter Your Password: ")
    isUserExists = False
    for user in basket.user_lst:
      if user['username'] == name and user['password'] == password:
        isUserExists = True
        break
    if isUserExists: # valid user
      while True:
        print("1. Add Item to your cart\n2. Update Your Cart\n3. Delete Your Cart\n4. Show Your Cart")
        choice = int(input("Enter your choice: "))
        if choice == 1:
          basket.addItemToCart(name)
        elif choice == 2:
          basket.updateProductCart(name)
        elif choice == 3:
          itemId = input("Enter Item ID: ")
          basket.deleteProductCart(name,itemId)
        elif choice == 4:
          basket.showDatabase()
        else:
          break

    else:
      print("Who You are? ")



    





# a = {"rakib":[{"itemID":12,"price":200}]}
# a['rakib'].append({"item":13})

# for i in a['rakib']:
#   if(i['itemID'] == 12):
#     a['rakib'].remove(i)
# print(a['rakib'])