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






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
