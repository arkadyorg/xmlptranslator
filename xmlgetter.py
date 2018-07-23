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
