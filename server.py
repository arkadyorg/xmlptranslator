from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Index page"

@app.route("/config")
def config():
	return "Config page"

@app.route("/about")
def about():
	return "About page"

if __name__ == "__main__":
	app.run()