from flask import Flask

app = Flask(__name__)

def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def main():
  return hello_world()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)