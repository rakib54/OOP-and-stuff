from flask import Flask, request

app = Flask(__name__)

data = {"rakib": '54'}

@app.route('/', methods=['GET'])
def home():
  return "This is home page"

@app.route('/about', methods=['GET'])
def about():
  return "This is about page"

@app.route('/get_data', methods=['GET'])
def get_data():
  return data

# add_data/?key=value
@app.route('/add_data', methods=['GET', 'PUT'])
def add_data():
  key, value = list(request.args.items())[0]
  data[key] = value
  return f"{key} added"


@app.route('/delete_data', methods=['GET', 'DELETE'])
def delete_data():
  key, value = list(request.args.items())[0]
  data.pop(value)
  return f"{key} deleted"

if __name__ == '__main__':
  app.run()