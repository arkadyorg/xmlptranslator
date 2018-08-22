import os, fnmatch, collections 
from dblogic import report_reindex, report_filepointer_select, template_reindex, parameters_reindex, report_dir_translist, language_code_by_id, template_dir_translist
from xmlgetter import template_lister, parameters_lister, default_template
from fileconsistency import file_copy
import settings
from xmlupdater import xdo_copy_translate


def report_reindex_igniter():
	exlist = ['*.xdo']

	for root, directories, filenames in os.walk('./original/'):
		for extensions in exlist:
			for filename in fnmatch.filter(filenames, extensions):
				title = (os.path.join(filename)).replace(".xdo", "")
				report_directory = (os.path.join(root))
				file_name = (os.path.join(filename))
				full_dir = default_template(os.path.join(root, filename))
				for a in full_dir:
					dt = (a['default'])
				report_reindex(title, report_directory, file_name, dt)

def template_reindex_igniter():
	filepointers = report_filepointer_select()
	for key, value in filepointers.items():
		template_result = template_lister(key,value)
		for template_entries in template_result:
			template_reindex(template_entries['td_report_id'], template_entries['td_template_label'], template_entries['td_template_type'], template_entries['td_template_url'], template_entries['td_template_lang'])

def parameters_reindex_igniter():
	filepointers = report_filepointer_select()
	for key, value in filepointers.items():
		parameters_result = parameters_lister(key,value)
		for parameters_entries in parameters_result:
			parameters_reindex(parameters_entries['pl_report_id'], parameters_entries['pl_param_id'], parameters_entries['pl_param_lable'])

def xdo_local_out_copy(lang_id):
	target_dir = settings.target_dir
	original_dir = settings.original_dir
	lang_code = language_code_by_id(lang_id)
	raw_data = report_dir_translist(lang_id)
	for report in raw_data:
		end_dir = report['original_dir'].replace(report['original_name'], report['local_name'])
		final_dir = end_dir.replace(original_dir, target_dir + lang_code + '/' )
		file_copy(report['original_dir'], (report['original_name']+'.xdo'), final_dir, (report['local_name']+'.xdo'))

def tmpl_local_out_copy(lang_id):
	target_dir = settings.target_dir
	original_dir = settings.original_dir
	lang_code = language_code_by_id(lang_id)
	raw_data = template_dir_translist(lang_id)
	for report in raw_data:
		end_dir = report['original_dir'].replace(report['report_original_name'], report['report_local_name'])
		final_dir = end_dir.replace(original_dir, target_dir + lang_code + '/' )
		file_copy(report['original_dir'], (report['original_file']), final_dir, (report['local_file']))

def xdo_local_translate_out_copy(report_id, lang_id):
	target_dir = settings.target_dir
	original_dir = settings.original_dir
	lang_code = language_code_by_id(lang_id)
	raw_data = report_dir_translist(lang_id)
	for report in raw_data:
		end_dir = report['original_dir'].replace(report['original_name'], report['local_name'])
		final_dir = end_dir.replace(original_dir, target_dir + lang_code + '/' )
		xdo_copy_translate(report_id, lang_code, report['original_dir'], (report['original_name']+'.xdo'), final_dir, (report['local_name']+'.xdo'))
