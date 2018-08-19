from flask import Flask, render_template, request, redirect, url_for
from dblogic import language_list, report_list, report_info_dtls_list, report_info_params_list, report_info_templ_list, update_report_local_name, language_id_by_code, update_param_local_name

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
	language_id = language_id_by_code(lang_code)
	report_name = report_info_dtls_list(id, lang_code)
	params_list = report_info_params_list(id, lang_code)
	templ_list = report_info_templ_list(id, lang_code)
	return render_template('reportconfig.html', reports=reports_list, language=lang_code, id=id, report_name=report_name, params_list=params_list, templ_list=templ_list, language_id=language_id)

@app.route("/post_report", methods = ['POST'])
def post_report():
	param_catcher = []

	report_id = request.args['report_id']
	lang_id = request.args['lang_id']
	language = request.args['language']

	params_list = report_info_params_list(report_id, language)
	for item in params_list:
		param_name = request.form.getlist('param_input_name'+ str(item['param_id']))
		param_id = item['param_id']
		update_param_local_name(param_id, param_name[0])

	print('ok')



	#test_get_params = request.form.getlist('param_input_name')
	#print(test_get_params)
	update_report_local_name(report_id,lang_id,request.form['rep_input_name'])

	return redirect(url_for('report_edit', lang_code=request.args['language'], id = request.args['report_id']))

if __name__ == "__main__":
	app.run(port=1111, debug=True)