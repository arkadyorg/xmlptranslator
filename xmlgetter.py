import xml.etree.ElementTree as ET  

def templates_list(file_pointer):
	tree = ET.parse(file_pointer)
	root = tree.getroot()
	for template_label in root.iterfind('./{http://xmlns.oracle.com/oxp/xmlp}templates//'):
		label = template_label.attrib
		print (label.get('label'))

def parameters_list(file_pointer):
	tree = ET.parse(file_pointer)
	root = tree.getroot()
	for template_param in root.iterfind('./{http://xmlns.oracle.com/oxp/xmlp}parameters//'):
		label = template_param.attrib
		if 'label' in label:
			param_lable = label.get('label')
			print (param_lable)
		else:
			pass

def report_title(file_pointer):
	tree = ET.parse(file_pointer)
	root = tree.getroot()
	return (root[0].text)

def default_template(file_pointer):
	default_template = []
	tree = ET.parse(file_pointer)
	root = tree.getroot()
	for a in root.iterfind('./{http://xmlns.oracle.com/oxp/xmlp}templates'):
		default_template.append({'default': a.attrib.get('default')})
	return default_template

def template_lister(rep_id, file_pointer):
	tree = ET.parse(file_pointer)
	root = tree.getroot()
	i = 0
	template_data = []
	for template_label in root.iterfind('./{http://xmlns.oracle.com/oxp/xmlp}templates//'):
		i += 1
		label = template_label.attrib
		p = label.get('label')[-2:]
		template_item = {'td_entry_num':i, 'td_report_id':rep_id, 'td_template_label': label.get('label'),'td_template_type':label.get('type'),'td_template_url':label.get('url'), 'td_template_lang': p.upper() }
		template_data.append(template_item)
	return template_data

def parameters_lister(rep_id, file_pointer):
	tree = ET.parse(file_pointer)
	root = tree.getroot()
	i = 0
	param_list = []
	for param in root.iterfind('./{http://xmlns.oracle.com/oxp/xmlp}parameters//'):
		label = param.attrib
		id = param.attrib
		param_lable=''
		if 'id' in id:
			param_id = id.get('id')
		elif 'label' in label:
			param_lable = label.get('label')
			i+=1
			param_item = {'pl_entry_num':i,'pl_report_id': rep_id, 'pl_param_id':param_id, 'pl_param_lable':param_lable}
			param_list.append(param_item)
		else:
			pass
	return param_list


