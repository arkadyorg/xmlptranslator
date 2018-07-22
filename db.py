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
    report_name = Column(String(100))
    report_dir = Column(String(300))
    file_name = Column(String(100))
    base_template = Column(String(100))
    base_lang = Column(String(100))
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



if __name__ == "__main__":
	Base.metadata.create_all(bind=engine)