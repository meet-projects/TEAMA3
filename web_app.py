from flask import Flask, render_template, flash
from flask import session as web_session
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
	if 'username' in web_session:
		user = session.query(User).filter_by(username = 'username').first()
		return render_template('home_page.html', user = user)
	return render_template('home_page.html')

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
	if request.method == 'GET':
		return render_template('sign_up.html')
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

@app.route('/sign_in', methods = ['GET','POST'])
def sign_in():
	if request.method == 'GET':
		return render_template("log_in.html")
	else:
		user = session.query(User).filter_by(username = request.form['username']).first()
		if user.username == None or user.password != request.form['password']:
			flash ("Invalid username or password")
		else:
			web_session['username'] = request.form['username']
			return redirect(url_for('main'))







@app.route('/examples')
def examples():
	pairs = session.query(Pair).all()
	return render_template('learn_more.html', pairs)



@app.route('/profile')
def profile():
	if 'username' in web_session:
		user = user = session.query(User).filter_by(username = 'username').first()
		return render_template("profile.html", user)
	else:
		flash ("You need to be logged in to view your profile")
		return redirect(url_for('main'))
		


@app.route('/profile/edit', methods = ['GET', 'POST'])
def profile_edit():
	if request.method == 'GET':
		if 'username' in web_session:
			user = session.query(User).filter_by(username = 'username').first()
			return render_template("PLACEHOLDER_PROFILE_EDIT.HTML", user)
		else:
			flash("You need to be logged in to edit your profile")
			return redirect(url_for('sign_in'))
	else:
			new_first_name = request.form['first_name']
			new_last_name = request.form['last_name']
			new_gender = request.form['gender']
			new_country = request.form['country']
			new_city = request.form['city']
			new_dob = request.form['dob']
			new_description = request.form['description']
			new_cultural_heritage = request.form['cultural_heritage']
			new_email = request.form['email']
			new_status = request.form['status']
			new_username = request.form['username']
			new_password = request.form['password']
			user.first_name = new_first_name
			user.last_name = new_last_name
			user.gender = new_gender
			user.country = new_country
			user.city = new_city
			user.dob = new_dob
			user.description = new_description
			user.cultural_heritage = new_cultural_heritage
			user.email = new_email
			user.status = new_status
			user.username = new_username
			user.password = new_password
			session.commit()
			return redirect(url_for('profile'))


if __name__ == '__main__':
    app.run(debug=True)
