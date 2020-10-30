"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect)
from model import connect_to_db
import crud
import os

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def get_homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def show_all_movies():
    """View all movies."""

    movies = crud.return_all_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    """Show details on specific movies"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/all-users')
def show_all_users():
    """View all users."""

    users = crud.return_all_users()

    return render_template('all_users.html', users=users)

@app.route('/all-users/<user_id>')
def user_details(user_id):
    """Show details on specific movies"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)

@app.route('/users', methods = ['POST'] )
def register_user():
    """Get inputs from form"""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if user == None:
        crud.create_user(email, password)
        flash('Account created! You can now log in.')
    else:    
        flash('Email already exists. Try again.')

    return redirect('/')

@app.route('/login', methods = ['POST'])
def log_in():
    """Gets input from log-in and checks to see if emails and passwords
    match."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if email == user.email and password == user.password:
        session['user'] = user.user_id
        flash('Logged in!')
    else:
        flash('Email and password do not match.')
    
    return redirect('/')
    


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
