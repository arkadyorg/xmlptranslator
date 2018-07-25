from db import db_session, Reports
from datetime import datetime


def report_reindex(r_name,r_dir,r_file):
	exists = db_session.query(Reports.report_name).filter_by(report_name=r_name).scalar() is not None
	if exists == False:
		report_item=Reports(report_name=r_name, report_dir=r_dir, file_name=r_file, created=datetime.now(), updated=datetime.now())
		db_session.add(report_item)
		db_session.commit()
	else:
		pass