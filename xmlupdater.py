from dblogic import param_translation_list, template_translation_list
import shutil
import os

def xdo_copy_translate(report_id, lang_code, source_dir, source_file, target_dir, target_file):
	param_translist = {}
	templ_translist = {}
	p_translations = param_translation_list(report_id,lang_code)
	t_trnaslations = template_translation_list(report_id,lang_code)
	for a in p_translations:
		param_translist['label="'+ a['base_name']] = 'label="'+ a['translated_name']
	for b in t_trnaslations:
		templ_translist['templates default="'+ b['base_name']] = 'templates default="'+ b['translated_name']
	with open((os.path.join(source_dir, source_file)), encoding='utf-8') as infile, open((os.path.join(target_dir, target_file)), 'w', encoding='utf-8') as outfile:
	    for line in infile:
	        for src, target in param_translist.items():
	            line = line.replace(src, target)
	        for src, target in templ_translist.items():
	            line = line.replace(src, target)
	        outfile.write(line)
