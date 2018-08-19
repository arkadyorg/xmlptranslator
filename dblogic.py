from db import db_session, Reports, Templates, Parameters, Languages, report_strings, param_strings, templ_strings
from datetime import datetime
import xml.etree.ElementTree as ET

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#	Commit functions
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def report_reindex(r_name,r_dir,r_file):
	exists = db_session.query(Reports.report_name).filter_by(report_name=r_name).scalar() is not None
	if exists == False:
		report_item=Reports(report_name=r_name, report_dir=r_dir, file_name=r_file, created=datetime.now(), updated=datetime.now())
		db_session.add(report_item)
		db_session.commit()
	else:
		pass

def template_reindex(rep_id,t_label,t_type,t_url,t_lang):
	exists = db_session.query(Templates.template_label).filter_by(template_label=t_label).scalar() is not None
	if exists == False:	
		template_item=Templates(report_id=rep_id, template_label=t_label, template_type=t_type, template_url=t_url, template_lang=t_lang, created=datetime.now(), updated=datetime.now())
		db_session.add(template_item)
		db_session.commit()
	else:
		pass

def parameters_reindex(rep_id, param_id, param_lable):
	exists = db_session.query(Parameters).filter_by(report_id=rep_id, parameter_id=param_id).scalar() is not None
	if exists == False:
		parameter_item=Parameters(report_id=rep_id, parameter_id=param_id, parameter_label=param_lable, created=datetime.now(), updated=datetime.now())
		db_session.add(parameter_item)
		db_session.commit()
	else:
		pass	

def language_add(l_locale, l_name, l_code):
	exists = db_session.query(Languages.locale).filter_by(locale=l_locale).scalar() is not None
	if exists == False:
		language_entry=Languages(locale=l_locale, name=l_name, code=l_code, created=datetime.now(), updated=datetime.now())
		db_session.add(language_entry)
		db_session.commit()
	else:
		pass

def reports_name_strings_reindex(r_id,l_id):
	exists = db_session.query(report_strings).filter_by(report_id=r_id, lang_id=l_id).scalar() is not None
	if exists == False:
		report_local_name=report_strings(report_id=r_id, lang_id=l_id, created=datetime.now(), updated=datetime.now())
		db_session.add(report_local_name)
		db_session.commit()
	else:
		pass

def parameters_lable_strings_reindex(p_id,l_id):
	exists = db_session.query(param_strings).filter_by(param_id=p_id, lang_id=l_id).scalar() is not None
	if exists == False:
		parameter_local_name=param_strings(param_id=p_id, lang_id=l_id, created=datetime.now(), updated=datetime.now())
		db_session.add(parameter_local_name)
		db_session.commit()
	else:
		pass

def templates_lable_strings_reindex(t_id, l_id):
	exists = db_session.query(templ_strings).filter_by(template_id=t_id, lang_id=l_id).scalar() is not None
	if exists == False:
		template_local_name=templ_strings(template_id=t_id, lang_id=l_id, created=datetime.now(), updated=datetime.now())
		db_session.add(template_local_name)
		db_session.commit()
	else:
		pass

def update_report_local_name(rep_id, lang_id, local_name):
	db_session.query(report_strings).filter(report_strings.report_id == rep_id, report_strings.lang_id == lang_id).update({'local_name': local_name, 'updated': datetime.now()})
	db_session.commit()

def update_param_local_name(par_string_id, local_name):
	db_session.query(param_strings).filter(param_strings.id == par_string_id).update({'data': local_name, 'updated': datetime.now()})
	db_session.commit()

def update_template_default(rep_id, lang_id, local_template):
	db_session.query(report_strings).filter(report_strings.report_id == rep_id, report_strings.lang_id == lang_id).update({'default_template': local_template, 'updated': datetime.now()})
	db_session.commit()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#	Read functions
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def report_filepointer_select():
	pointers_list = {}
	for instance in Reports.query.order_by(Reports.id): 
		pointers_list[instance.id] = (instance.report_dir +'/'+ instance.file_name)
	return pointers_list

def language_list():
	language_list = []
	for instance in Languages.query.order_by(Languages.id):
		language_list.append({'code':instance.code, 'name':instance.name})
	return language_list

def language_id_by_code(code):
	for instance in db_session.query(Languages).filter(Languages.code == code):
		lang_i = instance.id
	return(lang_i)

def report_list():
	report_list = []
	for instance in Reports.query.order_by(Reports.report_name):
		report_list.append({'id':instance.id, 'name':instance.report_name})
	return report_list

def default_templ_info(report_id, lang_id):
	default_template = []
	for instance in db_session.query(report_strings).filter(report_strings.report_id == report_id, report_strings.lang_id == lang_id):
		default_template.append({'string_id': instance.id, 'default_template': instance.default_template})
	return default_template

def report_info_dtls_list(report_id, lang_code):
	report_data = []
	report_n = '' 	# report name
	lang_i = ''		# language number
	report_loc =''	# report localisation name id
	for instance in db_session.query(Reports).filter(Reports.id == report_id):
		report_n = instance.report_name 
	for instance in db_session.query(Languages).filter(Languages.code == lang_code):
		lang_i = instance.id

	qa=db_session.query(Reports,report_strings).filter(Reports.id == report_id, Reports.id == report_strings.report_id, report_strings.lang_id == lang_i).all()
	for report_name_data in qa:
		report_data.append({'base_name' : report_name_data.Reports.report_name, 'translated_name' : report_name_data.report_strings.local_name})

	return report_data

def report_info_params_list(report_id, lang_code):
	report_data = []
	report_n = '' 	# report name
	lang_i = ''		# language number
	report_loc =''	# report localisation name id
	for instance in db_session.query(Reports).filter(Reports.id == report_id):
		report_n = instance.report_name 
	for instance in db_session.query(Languages).filter(Languages.code == lang_code):
		lang_i = instance.id

	qa=db_session.query(Parameters,param_strings).filter(Parameters.report_id == report_id, Parameters.id == param_strings.param_id, param_strings.lang_id==lang_i).all()
	for paramdata in qa:
		report_data.append({'param_id' : paramdata.param_strings.id, 'base_name' : paramdata.Parameters.parameter_label, 'translated_name' : paramdata.param_strings.data})

	return report_data


def report_info_templ_list(report_id, lang_code):
	report_data = []
	report_n = '' 	# report name
	lang_i = ''		# language number
	report_loc =''	# report localisation name id
	for instance in db_session.query(Reports).filter(Reports.id == report_id):
		report_n = instance.report_name 
	for instance in db_session.query(Languages).filter(Languages.code == lang_code):
		lang_i = instance.id

	qa=db_session.query(Templates, templ_strings).filter(Templates.report_id == report_id, Templates.id == templ_strings.template_id).all()
	for tlist in qa:
		report_data.append({'template_name' : tlist.Templates.template_label, 'string_id' : tlist.templ_strings.id, 'translated_name': tlist.templ_strings.data})

	return report_data

