from dblogic import dictionary_writer, dictionary_report_naming_miner, dictionary_report_parameters_miner

lang = 2
report_names_translist = dictionary_report_naming_miner(lang)

report_parameters_translist = dictionary_report_parameters_miner(lang)

for item in report_names_translist:
	dictionary_writer(item['lang_id'], item['datatype'], item['original'], item['translation'])

for item in report_parameters_translist:
	dictionary_writer(item['lang_id'], item['datatype'], item['original'], item['translation'])