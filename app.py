from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Connection db
database = 'flask-mysql'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/' + database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Settings 
CORS(app)

# Routes
from src.routes.tareasRoutes import *

# Starting Server
if __name__ == '__main__':
    app.run(debug=True, port=3344)




