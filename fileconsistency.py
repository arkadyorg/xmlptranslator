#! /usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os
import re
from dblogic import report_dir_translist, language_code_by_id, language_id_by_code
import settings

def local_dir_naming(lang_id):
	target_dir = settings.target_dir
	original_dir = settings.original_dir
	lang_code = language_code_by_id(lang_id)
	raw_data = report_dir_translist(lang_id)
	replacements =[]
	for report in raw_data:
		end_dir = report['original_dir'].replace(report['original_name'], report['local_name'])
		final_dir = end_dir.replace(original_dir, target_dir + lang_code + '/' )
		if not os.path.exists(final_dir):
			os.makedirs(final_dir)

def base_templates_extract_dir_naming(base_lang, pre_lang):
	target_dir = settings.prelang_dir
	original_dir = settings.original_dir
	lang_id = language_id_by_code(base_lang)
	raw_data = report_dir_translist(lang_id)
	for report in raw_data:
		end_dir = report['original_dir'].replace(report['original_name'], report['local_name'])
		final_dir = end_dir.replace(original_dir, target_dir + pre_lang + '/' )
		if not os.path.exists(final_dir):
			os.makedirs(final_dir)


def file_copy(source_dir, source_file, target_dir, target_file):
 	shutil.copyfile((os.path.join(source_dir, source_file)), (os.path.join(target_dir, target_file)))


def file_pe_rename(final_dir, local_name, base_lang, pre_lang):
	target_string = base_lang + '.rtf'
	replacement_string = pre_lang + '.rtf'
	ignorance_target_string = re.compile(target_string, re.IGNORECASE)
	new_name = (ignorance_target_string.sub(replacement_string,local_name))
	old_file = os.path.join(final_dir, local_name)
	new_file = os.path.join(final_dir, new_name)
	os.rename(old_file, new_file)