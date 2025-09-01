from flask import Flask, redirect, request
import os

app = Flask(__name__)

@app.route("/")
def main():
  #return "asd"
  return redirect("https://redisnotblue.up.railway.app" + request.path, code=301)

if __name__ == "__main__":
  app.run(port=os.environ.get("PORT", 5000)
