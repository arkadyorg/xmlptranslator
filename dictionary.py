#! /usr/bin/env python
# -*- coding: utf-8 -*-

from dblogic import dictionary_writer, dictionary_report_naming_miner, dictionary_report_parameters_miner, dictionary_report_name_getter, update_report_local_name, dictionary_report_parameters_getter, update_param_local_name

def dictionary_refresh(lang_id):
    report_names_translist = dictionary_report_naming_miner(lang_id)
    report_parameters_translist = dictionary_report_parameters_miner(lang_id)
    for item in report_names_translist:
        dictionary_writer(item['lang_id'], item['datatype'], item['original'], item['translation'])

    for item in report_parameters_translist:
        dictionary_writer(item['lang_id'], item['datatype'], item['original'], item['translation'])

def report_names_autotranslate(lang_id):
    report_missed_translations = dictionary_report_name_getter(lang_id)
    for report in report_missed_translations:
        update_report_local_name(report['report_id'], report['lang_id'], report['dictionary_answer'])

def report_parameters_autotranslate(lang_id):
    report_missed_translations = dictionary_report_parameters_getter(lang_id)
    for parameter in report_missed_translations:
        update_param_local_name(parameter['translated_item_id'], parameter['dictionary_answer'])
