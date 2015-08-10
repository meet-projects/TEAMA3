from flask import Flask, render_template, flash, request, redirect, url_for
from flask import session as web_session
from os import urandom
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base, User, Example, Pair
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


test = Example(
	content = "Culturebox taught me about different cultures and gave me an enjoyable activity to look forward to each month. I received many amazing gifts and learned much about both myself and others.",
	title = 'Culturebox changed my life!')
session.add(test)
session.commit()