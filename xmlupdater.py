import xml.etree.ElementTree as ET

file_pointer = "0102 Балансы счетов детально.xdo"
tree = ET.parse(file_pointer)
root = tree.getroot()

for template_param in root.iterfind('./{http://xmlns.oracle.com/oxp/xmlp}parameters//'):
	label = template_param.attrib
	if 'label' in label:
		param_lable = label.get('label')
		print (param_lable)
	else:
		pass