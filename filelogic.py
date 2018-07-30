import os, fnmatch, collections 
from dblogic import report_reindex, report_filepointer_select, template_reindex
from xmlgetter import template_lister



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
		print(template_result['td_report_id'], template_result['td_template_label'], template_result['td_template_type'], template_result['td_template_url'], template_result['td_template_lang'])
	print('ok')