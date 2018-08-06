import os, fnmatch, collections 
from dblogic import report_reindex, report_filepointer_select, template_reindex, parameters_reindex
from xmlgetter import template_lister, parameters_lister



def report_reindex_igniter():
	exlist = ['*.xdo']

	for root, directories, filenames in os.walk('./original/'):
		for extensions in exlist:
			for filename in fnmatch.filter(filenames, extensions):
				title = (os.path.join(filename)).replace(".xdo", "")
				report_directory = (os.path.join(root))
				file_name = (os.path.join(filename))
				report_reindex(title, report_directory, file_name)

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

def reportnames_reindex_igniter():
	