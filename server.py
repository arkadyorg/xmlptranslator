from flask import Flask, render_template
from dblogic import language_list, report_list, report_edit_data_list

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
	return render_template('reportlist.html', reports=result, language=lang_code)

@app.route("/language/<lang_code>/<id>")
def report_edit(lang_code, id):
	reports_list = report_list()
	report_data = report_edit_data_list(id, lang_code)
	base_name = report_data['Report']['base name']
	translated_name = report_data['Report']['translated name']
	params = report_data['Parameters']
	return render_template('reportconfig.html', reports=reports_list, language=lang_code, id=id, report_data=report_data, base_name=base_name, translated_name=translated_name, paramlist=params)

if __name__ == "__main__":
	app.run(port=1111, debug=True)