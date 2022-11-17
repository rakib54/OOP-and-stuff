from flask import Flask,request

app = Flask(__name__)

data ={"shakib": "75", "Rakibur": "74"}

@app.route("/", methods=["GET"])
def Home():
  return "This is home page"

app.add_url_rule("/get_data", endpoint="get_data")
@app.endpoint("get_data")
def get_data():
  return data

app.add_url_rule("/add_data", endpoint="add_data",methods=['POST'])
@app.endpoint("add_data")
def add_data():
  key, value = list(request.args.items())[0]
  if key not in data.keys():
    data[key] = value
    return f"{key} added successfully"
  else:
    return f"{key} already exists"
  
app.add_url_rule("/update",endpoint="update",methods=['PUT'])
@app.endpoint("update")
def update_data():
  key, value = list(request.args.items())[0]
  if key in data.keys():
    data[key] = value
    return f"{key} value updated"
  else:
    return f"{key} is not found"
  

app.add_url_rule("/delete_data", endpoint="delete_data",methods=['DELETE'])
@app.endpoint("delete_data")
def delete_data():
  key,value = list(request.args.items())[0]
  if value in data:
    data.pop(value)
    return f"{value} deleted successfully"
  else:
    return f"User not found"
  

if __name__ == "__main__":
  app.run()