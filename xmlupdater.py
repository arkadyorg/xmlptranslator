from dblogic import translation_list
import shutil
import os

def xdo_copy_translate(report_id, lang_code, source_dir, source_file, target_dir, target_file):
	translist = {}
	translations = translation_list(report_id,lang_code)
	for a in translations:
		translist['label="'+ a['base_name']] = 'label="'+ a['translated_name']
	with open((os.path.join(source_dir, source_file)), encoding='utf-8') as infile, open((os.path.join(target_dir, target_file)), 'w', encoding='utf-8') as outfile:
	    for line in infile:
	        for src, target in translist.items():
	            line = line.replace(src, target)
	        outfile.write(line)