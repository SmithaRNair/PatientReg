from sqlalchemy import create_engine
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL= "mysql+mysqlconnector://root:1234@localhost/patientdb"
engine=create_engine(DATABASE_URL)
Sessionlocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
