from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ammt-dev11'

from SearchRecipes_Flask import routes
