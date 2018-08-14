from flask import Flask, render_template
from dblogic import language_list, report_list

app = Flask(__name__)

@app.route("/")
def index():
	result = language_list()
	return render_template('index.html', languages=result)

@app.route("/config")
def config():
	return "Config page"

@app.route("/about")
def about():
	return "About page"

@app.route("/language/<lang_code>")
def reports_by_lang(lang_code):
	result = report_list()
	
	names = ''
	for repname in result:
		names = names + '<p>' + repname['name'] + '</p>'
	return str(names)
	
	#return render_template('index.html', languages=result)

if __name__ == "__main__":
	app.run(port=1234, debug=True)