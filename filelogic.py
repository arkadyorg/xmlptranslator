import xml.etree.ElementTree as ET  
tree = ET.parse('0201 Birth dates.xdo')
root = tree.getroot()
'''
for item in root.iterfind('./{http://xmlns.oracle.com/oxp/xmlp}parameters//'):
    print('ITEM TAG:: {}, ITEM KEYS:: {} ITEM ITEMS:: {} ITEM TEXT:: {} '.format(item.tag, item.keys(), item.items(), item.text))

'''
for item in root.iterfind('./{http://xmlns.oracle.com/oxp/xmlp}templates//'):
    print('ITEM TAG:: {}, ITEM KEYS:: {} ITEM ITEMS:: {} ITEM TEXT:: {} '.format(item.tag, item.keys(), item.items(), item.text))
    