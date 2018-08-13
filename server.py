from flask import Flask
from dblogic import language_list

app = Flask(__name__)

@app.route("/")
def index():
	result = language_list()
	names =''
	for langname in result:
		#names =  names + langname['name']
		#<p><a href="url">link text</a></p>
		names = names + '<p><a href="/language/' + langname['code'] + '">'+ langname['name']  +'</a></p>'
	return str(names)

@app.route("/config")
def config():
	return "Config page"

@app.route("/about")
def about():
	return "About page"

@app.route("/language/<lang_code>")
def reports_by_lang(lang_code):
	return 'Language %s' % lang_code

if __name__ == "__main__":
	app.run(port=1234, debug=True)