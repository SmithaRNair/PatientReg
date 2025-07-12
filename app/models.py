from sqlalchemy import Column, Integer, String
from .database import Base

class Patient(Base):
    __tablename__="patients"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(30))
    age=Column(Integer)
    gender=Column(String(7))
    doctor=Column(String(30))
    disease=Column(String(25)) 
    