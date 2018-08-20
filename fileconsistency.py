import shutil
import os
from dblogic import report_dir_translist, language_code_by_id

#target_dir = "out/"
#original_dir = "original/"
#lang_id = 2
def local_dir_naming(lang_id):
	lang_code = language_code_by_id(lang_id)
	raw_data = report_dir_translist(lang_id)

	#print (raw_data)
	replacements =[]
	for report in raw_data:
		end_dir = report['original_dir'].replace(report['original_name'], report['local_name'])
		final_dir = end_dir.replace(original_dir, target_dir + lang_code + '/' )
		#print(final_dir)
		if not os.path.exists(final_dir):
			os.makedirs(final_dir)
