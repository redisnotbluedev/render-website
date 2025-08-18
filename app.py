from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def main():
  #return "asd"
  return redirect("https://redisnotblue.up.railway.app", code=301)


app.run()
