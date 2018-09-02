from flask import Flask, render_template, request, redirect, url_for
from dblogic import (
                    language_list, report_list, report_info_dtls_list,
                    report_info_params_list, report_info_templ_list,
                    update_report_local_name, language_id_by_code,
                    update_param_local_name, update_template_default,
                    default_templ_info, report_list_issue_bylang,
                    language_code_by_id)
from fileconsistency import local_dir_naming
from filelogic import xdo_local_translate_out_copy, tmpl_local_out_copy
from dictionary import dictionary_refresh

app = Flask(__name__)


@app.route("/")
def index():
    result = language_list()
    return render_template('index.html', languages=result)


@app.route("/export")
def export():
    return "Export page"


@app.route("/about")
def about():
    return "About page"


@app.route("/language/<lang_code>")
def reports_by_lang(lang_code):
    language_id = language_id_by_code(lang_code)
    result = report_list_issue_bylang(language_id)
    return render_template(
                            'reportlist.html', reports=result,
                            language=lang_code, language_id=language_id)


@app.route("/language/<lang_code>/<id>")
def report_edit(lang_code, id):
    language_id = language_id_by_code(lang_code)
    reports_list = report_list_issue_bylang(language_id)
    report_name = report_info_dtls_list(id, lang_code)
    params_list = report_info_params_list(id, lang_code)
    templ_list = report_info_templ_list(id, lang_code)
    default_templ = default_templ_info(id, language_id)
    return render_template(
                            'reportconfig.html', reports=reports_list,
                            language=lang_code, id=id, report_name=report_name,
                            params_list=params_list, templ_list=templ_list,
                            language_id=language_id,
                            default_templ=default_templ)


@app.route("/post_report", methods=['POST'])
def post_report():

    report_id = request.args['report_id']
    lang_id = request.args['lang_id']
    language = request.args['language']

    params_list = report_info_params_list(report_id, language)
    for item in params_list:
        param_name = request.form.getlist(
                                            'param_input_name' +
                                            str(item['param_id']))
        param_id = item['param_id']
        update_param_local_name(param_id, param_name[0])
    update_report_local_name(
                            report_id, lang_id,
                            request.form['rep_input_name'])
    default_template = request.form.getlist('options')
    if len(default_template) != 0:
        update_template_default(report_id, lang_id, default_template[0])
    else:
        pass

    return redirect(
                    url_for(
                            'report_edit', lang_code=request.args['language'],
                            id=request.args['report_id']))


@app.route("/export_reports", methods=['POST'])
def export_reports():
    lang_id = request.args['lang_id']
    lang_code = language_code_by_id(lang_id)
    report_lista = report_list()
    local_dir_naming(lang_id)
    dictionary_refresh(lang_id)
    for a in report_lista:
        xdo_local_translate_out_copy(a['id'],lang_id)
    tmpl_local_out_copy(lang_id)
    return redirect(
                    url_for(
                            'reports_by_lang', lang_code=lang_code))


if __name__ == "__main__":
    app.run(port=1111, debug=True)
