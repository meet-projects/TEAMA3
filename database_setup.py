from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
	__table__='users'
	id=Column(Integer, primary_key=True)
	first_name= Column(String)
	last_name= Column(String)
	gender= Column(String)
	country= Column(String)
	city= Column(String)
	dob=Column(Date)
	description=Column(String)
	cultual_heritage=Column(String)
	email=Column(String)
	status=Column(Boolean)
	username=Column(String)
	password=Column(String)

class Example(Base):
	__table__='examples'
	id=Column(Integer, primary_key=True)
	title=Column(String)
	user_id=Column(Integer)
	content=Column(String)
	image=Column(String)

class Pair(Base):
	__table__='pairs'
	id=Column(Integer, primary_key=True)
	id_1=Column(Integer)
	id_2=Column(Integer)






#PLACE YOUR TABLE SETUP INFORMATION HERE

