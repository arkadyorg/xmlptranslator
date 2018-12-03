#! /usr/bin/env python
# -*- coding: utf-8 -*-

from db import db_session, Reports, Templates, Parameters, Languages
from dblogic import reports_name_strings_reindex, parameters_lable_strings_reindex, templates_lable_strings_reindex
from datetime import datetime


def report_naming():
    ql = Languages.query.order_by(Languages.code).all()
    qr = Reports.query.order_by(Reports.report_name).all()
    qa = (db_session.query(Reports,Languages).all())
    for repinf in qa:
        reports_name_strings_reindex(repinf.Reports.id, repinf.Languages.id)


def parameters_lang_naming():
    ql = Languages.query.order_by(Languages.code).all()
    qp = Parameters.query.order_by(Parameters.parameter_id).all()
    qa = (db_session.query(Parameters,Languages).all())
    for paraminf in qa:
        parameters_lable_strings_reindex(paraminf.Parameters.id, paraminf.Languages.id)


def templates_lang_naming():
    ql = Languages.query.order_by(Languages.code).all()
    qt = Templates.query.order_by(Templates.id).all()
    qa=db_session.query(Templates.id,Languages.id).filter(Templates.template_lang == Languages.code).all()
    for templinf in qa:
        templates_lable_strings_reindex(templinf[0], templinf[1])
