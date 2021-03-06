#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import (
                        create_engine, Column, Integer, String, Text, DateTime,
                        ForeignKey, TIMESTAMP, update, and_)
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///OBItransbase.db')

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Reports(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    report_name = Column(String(254))  
    report_dir = Column(String(1000))  
    file_name = Column(String(254))  
    default_template = Column(String(150))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

    def __repr__(self): 
        return '<Report #{}: {}>'.format(self.id, self.report_name)


class Languages(Base):
    __tablename__ = 'language_list'
    id = Column(Integer, primary_key=True)
    locale = Column(String(100))
    name = Column(String(100))
    code = Column(String(100))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return '<Language space {} was created'.format(self.locale)


class Templates(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True)
    report_id = Column(Integer)
    template_label = Column(String(254))
    template_type = Column(String(254))
    template_url = Column(String(254))
    template_lang = Column(String(254))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return '<Template {} for {}>'.format(
                                            self.template_label,
                                            self.report_id)


class Parameters(Base):
    __tablename__ = 'parameters_list'
    id = Column(Integer, primary_key=True)
    report_id = Column(Integer)
    parameter_id = Column(String(100))
    parameter_label = Column(String(254))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return '<Parameters list for report {}>'.format(self.report_id)


class templ_strings(Base):
    __tablename__ = 'template_strings'
    id = Column(Integer, primary_key=True)
    template_id = Column(Integer)
    lang_id = Column(Integer)
    data = Column(String(254))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return '<Template strings list for report {}>'.format(self.report_id)


class param_strings(Base):
    __tablename__ = 'parameters_strings'
    id = Column(Integer, primary_key=True)
    param_id = Column(Integer)
    lang_id = Column(Integer)
    data = Column(String(254))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return '<Template strings list for report {}>'.format(self.report_id)


class report_strings(Base):
    __tablename__ = 'reports_strings'
    id = Column(Integer, primary_key=True)
    report_id = Column(Integer)  # original ID
    lang_id = Column(Integer)  # Lang ID
    local_name = Column(String(100))
    default_template = Column(String(254))  # default template to show
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return '<Template strings list for report {}>'.format(self.report_id)


class dictionary(Base):
    __tablename__ = 'dictionary_strings'
    id = Column(Integer, primary_key=True)
    lang_id = Column(Integer)  # Lang ID
    datatype = Column(Integer) # 1 Report name / 2 parameters / 3 Templates / 4 Deep / 5 Dir
    original = Column(String(254))
    translation = Column(String(254))
    lock = Column(String(50))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

class users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(254))
    pincode = Column(String(254))
    active = Column(Integer)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
