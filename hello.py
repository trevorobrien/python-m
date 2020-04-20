from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "TEST"

def add(x,y):
    return 2 + 2

if __name__ == "__main__":
	app.run()