from db import db_session, Reports
from datetime import datetime
import xml.etree.ElementTree as ET


def report_reindex(r_name,r_dir,r_file):
	exists = db_session.query(Reports.report_name).filter_by(report_name=r_name).scalar() is not None
	if exists == False:
		report_item=Reports(report_name=r_name, report_dir=r_dir, file_name=r_file, created=datetime.now(), updated=datetime.now())
		db_session.add(report_item)
		db_session.commit()
	else:
		pass

def template_reindex(rep_id,t_label,t_type,t_url,t_lang):
	template_item=Reports(report_id=rep_id, template_label=t_label, template_type=t_type, template_url=t_url, template_lang=t_lang, created=datetime.now(), updated=datetime.now())
	db_session.add(report_item)
	db_session.commit()

def report_filepointer_select():
	for instance in Reports.query.order_by(Reports.id): 
		print (instance.report_dir +'/'+ instance.file_name)