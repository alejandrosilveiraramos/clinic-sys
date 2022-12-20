from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_pyfile('core/config.py')

from core.views import *

if __name__ == '__main__' :
    app.run(debug=True)

