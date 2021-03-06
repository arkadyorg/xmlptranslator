#! /usr/bin/env python
# -*- coding: utf-8 -*-

from db import db_session, Reports, Templates, Parameters, Languages, report_strings, param_strings, templ_strings, dictionary, users
from sqlalchemy import or_
from datetime import datetime
import xml.etree.ElementTree as ET

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#	Commit functions
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def report_reindex(r_name,r_dir,r_file,r_deftempl):
	exists = db_session.query(Reports.report_name).filter_by(report_name=r_name).scalar() is not None
	if exists == False:
		report_item=Reports(report_name=r_name, report_dir=r_dir, file_name=r_file, default_template=r_deftempl, created=datetime.now(), updated=datetime.now())
		db_session.add(report_item)
		db_session.commit()
	else:
		pass

def template_reindex(rep_id,t_label,t_type,t_url,t_lang):
	exists = db_session.query(Templates).filter_by(template_label=t_label, report_id=rep_id).scalar() is not None
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


def dictionary_writer(lang_id, datatype, original, translation):
	exists = db_session.query(dictionary).filter_by(lang_id = lang_id, datatype = datatype, original = original, translation = translation).scalar() is not None
	if exists == False:
		translation_item = dictionary(lang_id = lang_id, datatype = datatype, original = original, translation = translation, created=datetime.now(), updated=datetime.now())
		db_session.add(translation_item)
		db_session.commit()
	else:
		pass		

def delete_reports_data():
	templ_strings.query.delete()
	param_strings.query.delete()
	report_strings.query.delete()
	Parameters.query.delete()
	Templates.query.delete()
	Reports.query.delete()
	db_session.commit()

def dictionary_reset():
	dictionary.query.delete()
	db_session.commit()

def dictionary_item_delete(id):
	db_session.query(dictionary).filter(dictionary.id == id).delete()
	db_session.commit()

def add_user(username, pincode):
	exists = db_session.query(users).filter_by(username=username, pincode=pincode).scalar() is not None
	if exists == False:
		new_user=users(username=username, pincode=pincode, active=1)
		db_session.add(new_user)
		db_session.commit()
	else:
		pass

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

def language_code_by_id(id):
	for instance in db_session.query(Languages).filter(Languages.id == id):
		lang_code = instance.code
	return(lang_code)

def report_list():
	report_list = []
	for instance in Reports.query.order_by(Reports.report_name):
		report_list.append({'id':instance.id, 'name':instance.report_name})
	return report_list

def report_list_issue_bylang(lang_id):
	report_list = []
	for instance in Reports.query.order_by(Reports.report_name):
		iss_report_names = db_session.query(report_strings).filter(report_strings.report_id == instance.id, report_strings.lang_id == lang_id).filter(or_(report_strings.local_name == None, report_strings.local_name == 'None', report_strings.local_name == '')).count()
		iss_param_names = db_session.query(Parameters, param_strings).filter(Parameters.report_id == instance.id, Parameters.id == param_strings.param_id, param_strings.lang_id == lang_id).filter(or_(param_strings.data == 'None', param_strings.data == None, param_strings.data == '')).count()
		iss_def_templ_names = db_session.query(report_strings).filter(report_strings.report_id == instance.id, report_strings.lang_id == lang_id).filter(or_(report_strings.default_template == None, report_strings.default_template == 'None', report_strings.default_template == '')).count()
		issue_sum = iss_report_names + iss_param_names + iss_def_templ_names
		for rs in db_session.query(report_strings).filter(report_strings.lang_id == lang_id, report_strings.report_id == instance.id).all():
			deftempl = rs.default_template
		report_list.append({'id':instance.id, 'name':instance.report_name, 'issues': issue_sum, 'naming_issue': iss_report_names, 'parameters_issue': iss_param_names, 'templates_issue': iss_def_templ_names, 'default_template': deftempl})
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

def report_dir_translist(lang_id):
	files_data = []
	qa=db_session.query(Reports, report_strings).filter(Reports.id == report_strings.report_id, report_strings.lang_id == lang_id, report_strings.local_name != None).all()
	for reports in qa:
		files_data.append({'report_id' : reports.Reports.id, 'original_name' : reports.Reports.report_name, 'original_dir' : reports.Reports.report_dir, 'original_file': reports.Reports.file_name, 'local_name': reports.report_strings.local_name})

	return files_data

def one_report_dir_translist(report_id, lang_id):
	files_data = []
	qa=db_session.query(Reports, report_strings).filter(Reports.id == report_strings.report_id, Reports.id == report_id, report_strings.lang_id == lang_id, report_strings.local_name != None).all()
	for reports in qa:
		files_data.append({'report_id' : reports.Reports.id, 'original_name' : reports.Reports.report_name, 'original_dir' : reports.Reports.report_dir, 'original_file': reports.Reports.file_name, 'local_name': reports.report_strings.local_name})
	return files_data


def template_dir_translist(lang_id):
	files_data = []
	qa=db_session.query(Reports, report_strings, Templates).filter(Reports.id == report_strings.report_id, report_strings.lang_id == lang_id, report_strings.local_name != None, Reports.id == Templates.report_id).all()
	for reports in qa:
		files_data.append({'report_id' : reports.Reports.id, 'report_original_name' : reports.Reports.report_name, 'report_local_name': reports.report_strings.local_name, 'original_dir' : reports.Reports.report_dir, 'original_file': reports.Templates.template_url, 'local_file': reports.Templates.template_url, 'templ_lang': reports.Templates.template_lang})

	return files_data

def param_translation_list(report_id, lang_code):
	translation_data = []
	report_n = '' 	# report name
	lang_i = ''		# language number
	report_loc =''	# report localisation name id
	for instance in db_session.query(Reports).filter(Reports.id == report_id):
		report_n = instance.report_name 
	for instance in db_session.query(Languages).filter(Languages.code == lang_code):
		lang_i = instance.id
	qa=db_session.query(Reports, report_strings, Parameters, param_strings).filter(Reports.id == report_strings.report_id, report_strings.lang_id == lang_i, report_strings.local_name != None, Parameters.report_id == Reports.id, Reports.id == report_id, param_strings.param_id == Parameters.id, param_strings.lang_id == lang_i).all()
	for data in qa:
		translation_data.append({'base_name': data.Parameters.parameter_label,'translated_name': data.param_strings.data})
	return translation_data

def template_translation_list(report_id, lang_code):
	translation_data = []
	report_n = '' 	# report name
	lang_i = ''		# language number
	report_loc =''	# report localisation name id
	for instance in db_session.query(Reports).filter(Reports.id == report_id):
		report_n = instance.report_name 
	for instance in db_session.query(Languages).filter(Languages.code == lang_code):
		lang_i = instance.id
	qa=db_session.query(Reports, report_strings).filter(Reports.id == report_strings.report_id, Reports.id == report_id, report_strings.lang_id == lang_i).all()
	for data in qa:
		translation_data.append({'base_name': data.Reports.default_template,'translated_name': data.report_strings.default_template})
	return translation_data

def dictionary_report_naming_miner(lang_id):
	translated_data = []
	qa=db_session.query(Reports, report_strings).filter(Reports.id == report_strings.report_id, report_strings.lang_id == lang_id, report_strings.local_name != None).all()
	for items in qa:
		translated_data.append({'lang_id' : items.report_strings.lang_id, 'datatype' : 1, 'original' : items.Reports.report_name, 'translation': items.report_strings.local_name})
	return translated_data

def dictionary_report_parameters_miner(lang_id):
	translated_data = []
	qa=db_session.query(Parameters, param_strings).filter(Parameters.id == param_strings.param_id, param_strings.lang_id == lang_id, param_strings.data != None).all()
	for items in qa:
		translated_data.append({'lang_id' : items.param_strings.lang_id, 'datatype' : 2, 'original' : items.Parameters.parameter_label, 'translation': items.param_strings.data})
	return translated_data

def dictionary_report_name_getter(lang_id):
	translated_data = []
	qa=db_session.query(Reports, report_strings, dictionary).filter(Reports.id == report_strings.report_id, report_strings.lang_id == lang_id, dictionary.lang_id == lang_id, Reports.report_name == dictionary.original, dictionary.datatype == 1).all()
	for items in qa:
		translated_data.append({'report_id' : items.Reports.id, 'lang_id' : lang_id, 'original' : items.Reports.report_name, 'current_translation' : items.report_strings.local_name, 'dictionary_answer' : items.dictionary.translation, 'translated_item_id': items.report_strings.id})
	return translated_data

def dictionary_report_parameters_getter(lang_id):
	translated_data = []
	qa=db_session.query(Parameters, param_strings, dictionary).filter(Parameters.id == param_strings.param_id, param_strings.lang_id == lang_id, dictionary.lang_id == lang_id, Parameters.parameter_label == dictionary.original, dictionary.datatype == 2).all()
	for items in qa:
		translated_data.append({'report_id' : items.Parameters.id, 'lang_id' : lang_id, 'original' : items.Parameters.parameter_label, 'current_translation' : items.param_strings.data, 'dictionary_answer' : items.dictionary.translation, 'translated_item_id': items.param_strings.id})
	return translated_data

def dictionary_data():
	dictionary_data = []
	qa=db_session.query(Languages, dictionary).filter(dictionary.lang_id == Languages.id).all()
	for items in qa:
		dictionary_data.append({'lang_code' : items.Languages.code, 'lang_name' : items.Languages.name, 'original' : items.dictionary.original, 'translation' : items.dictionary.translation, 'item_id':items.dictionary.id })
	return dictionary_data

