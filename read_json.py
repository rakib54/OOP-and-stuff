import json

class Product:
  allProduct = []

  def __init__(self,name,price):
    self.name = name
    self.price = price
    self.allProduct.append(self)

  @staticmethod
  def initialize_json():
    with open ("json.txt" , 'r') as file:
      data = file.read()
      json_data = json.loads(data)
      for product in json_data:
        Product(name = product["name"], price= product["price"])

  def __repr__(self):
    return f"Product({self.name} and price {self.price})"


Product.initialize_json()
print(Product.allProduct)

