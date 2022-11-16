from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return "This is home page"

@app.route('/about', methods=['GET'])
def about():
  return "This is about page"

if __name__ == '__main__':
  app.run()