from flask import Flask, render_template, session, flash
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base, User, Example, Pair
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

#YOUR WEB APP CODE GOES HERE

@app.route('/')
def main():
	return render_template('main_page.html')

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
	if request.method == 'GET':
		return render_template('PLACEHOLDER_SIGN_UP.HTML')
	else:
		new_user = User(
			first_name = request.form['first_name'],
			last_name = request.form['last_name'],
			gender = request.form['gender'],
			country = request.form['country'],
			city = request.form['city'],
			dob = request.form['dob'],
			description = request.form['description'],
			cultural_heritage = request.form['cultural_heritage'],
			email = request.form['email'],
			status = request.form['status'],
			username = request.form['username'],
			password = request.form['password'],
			)
		session.add(new_user)
		session.commit()
		return redirect(url_for('main'))

@app.route('/sign_in', methods = ['Get','POST'])
def sign_in():
	if request.method == 'GET':
		return render_template("PLACEHOLDER_SIGN_IN.HTML")
	else:
		user = session.query(User).filter_by(username = request.form['username']).first()
		if user.username == None or user.password != request.form['password']:
			flash ("Invalid username or password")
		else:
			session['username'] = request.form['username']







@app.route('/examples')
def examples():
	pairs = session.query(Pair).all()
	return render_template('PLACEHOLDER_EXAMPLES.HTML', pairs)






if __name__ == '__main__':
    app.run(debug=True)
