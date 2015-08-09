from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base, User, Example, Pair
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#YOUR WEB APP CODE GOES HERE

@app.route('/')
def main():
	return render_template('main_page.html')

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_in():
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
			user_name = request.form['user_name'],
			password = request.form['password'],
			)
		session.add(new_user)
		session.commit()
		return redirect(url_for('main'))


#@app.route('/sign_in')





if __name__ == '__main__':
    app.run(debug=True)
