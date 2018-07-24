from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, TIMESTAMP, update
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///OBItransbase.db')

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Reports(Base): 
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    report_name = Column(String(100)) #title
    report_dir = Column(String(300)) #without end file
    file_name = Column(String(100)) #full filename
    #default_template = Column(String(100)) 
    #base_lang = Column(String(100))
    created = Column(TIMESTAMP, nullable=False)
    updated = Column(TIMESTAMP, nullable=False)

    def __repr__(self): # внутри классов - методы 
        return '<Report #{}: {}>'.format(self.id, self.report_name)

class Languages(Base):
	__tablename__ = 'language_list'
	id = Column(Integer, primary_key=True)
	locale = Column(String(100))
	code = Column(String(100))
	created = Column(TIMESTAMP, nullable=False)
	updated = Column(TIMESTAMP, nullable=False)

	def __repr__(self):
		return '<Language space {} was created {} and updated {}>'.format(self.locale, self.created, self.updated)

class Templates(Base):
	__tablename__ = 'templates'
	id = Column(Integer, primary_key=True)
	report_id = Column(Integer)
	template_label = Column(String(100))
	template_type = Column(String(100))
	template_url = Column(String(100))
	template_lang = Column(String(100))
	created = Column(TIMESTAMP, nullable=False)
	updated = Column(TIMESTAMP, nullable=False)

	def __repr__(self):
		return '<Template {} for {}>'.format(self.template_label, self.report_id)

class Parameters(Base):
	__tablename__ = 'parameters_list'
	id = Column(Integer, primary_key=True)
	report_id = Column(Integer)
	base_label = Column(String(100))
	created = Column(TIMESTAMP, nullable=False)
	updated = Column(TIMESTAMP, nullable=False)

	def __repr__(self):
		return '<Parameters list for report {}>'.format(self.report_id)

class templ_strings(Base):
	__tablename__ = 'template_strings'
	id = Column(Integer, primary_key=True)
	report_id = Column(Integer)
	template_id = Column(Integer)
	lang_id = Column(Integer)
	data = Column(String(100))
	created = Column(TIMESTAMP, nullable=False)
	updated = Column(TIMESTAMP, nullable=False)

	def __repr__(self):
		return '<Template strings list for report {}>'.format(self.report_id)

class param_strings(Base):
	__tablename__ = 'parameters_strings'
	id = Column(Integer, primary_key=True)
	report_id = Column(Integer)
	param_id = Column(Integer)
	lang_id = Column(Integer)
	data = Column(String(100))
	created = Column(TIMESTAMP, nullable=False)
	updated = Column(TIMESTAMP, nullable=False)

	def __repr__(self):
		return '<Template strings list for report {}>'.format(self.report_id)

if __name__ == "__main__":
	Base.metadata.create_all(bind=engine)