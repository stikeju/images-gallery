from os import (environ)
from requests import (get)
from flask import (Flask, request)
from dotenv import (load_dotenv)

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = environ.get("UNSPLASH_KEY", "")
relative_path_env_local = "./.env.local"
app = Flask(__name__)

load_dotenv(dotenv_path=relative_path_env_local)


if not UNSPLASH_KEY:
  raise EnvironmentError("Please create .env.local file and insert there UNSPLASH_KEY")


def new_image():
  word = request.args.get("query")
  headers = {
    "Accept-Version": "v1",
    "Authorization" : f"Client-ID {UNSPLASH_KEY}"
  }
  params = {"query": word}
  response = get(url=UNSPLASH_URL, headers=headers, params=params)
  data = response.json()
  return data

@app.route("/new-image")
def main():
  return new_image()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)  