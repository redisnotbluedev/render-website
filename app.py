from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def main():
  #return "asd"
  return redirect("https://redisnotblue.up.railway.app" + request.path, code=301)


app.run()
