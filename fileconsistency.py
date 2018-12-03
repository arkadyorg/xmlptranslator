#! /usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os
from dblogic import report_dir_translist, language_code_by_id
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


def file_copy(source_dir, source_file, target_dir, target_file):
 	shutil.copyfile((os.path.join(source_dir, source_file)), (os.path.join(target_dir, target_file)))
