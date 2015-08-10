from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__='users'
	id=Column(Integer, primary_key=True)
	first_name= Column(String)
	last_name= Column(String)
	gender= Column(String)
	country= Column(String)
	city= Column(String)
	dob=Column(Date)
	description=Column(String)
	cultural_heritage=Column(String)
	email=Column(String)
	status=Column(Boolean)
	username=Column(String)
	password=Column(String)

class Example(Base):
	__tablename__='examples'
	id=Column(Integer, primary_key=True)
	title=Column(String)
	user_id=Column(Integer)
	content=Column(String)
	image=Column(String)

class Pair(Base):
	__tablename__='pairs'
	id=Column(Integer, primary_key=True)
	id_1=Column(Integer, ForeignKey('examples.id'))
	id_2=Column(Integer, ForeignKey('examples.id'))






#PLACE YOUR TABLE SETUP INFORMATION HERE

