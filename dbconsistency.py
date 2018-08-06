from db import db_session, Reports, Templates, Parameters, Languages
from dblogic import reports_name_strings_reindex
from datetime import datetime

def report_naming():
	ql = Languages.query.order_by(Languages.code).all()
	qr = Reports.query.order_by(Reports.report_name).all()
	qa = (db_session.query(Reports,Languages).all())
	for repinf in qa:
		reports_name_strings_reindex(repinf.Reports.id, repinf.Languages.id)