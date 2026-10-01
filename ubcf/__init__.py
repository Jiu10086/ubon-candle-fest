import os, secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ubcandle_db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ubcandledb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password><username>.mysql.pythonanywhere-services.com/<username>$<database_name>'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ubcf2026_en13_user:YdEtdPlwgsow8EJuJn86I4KriIakWv8N@dpg-daqafrou01pc73ff7h80-a.oregon-postgres.render.com/ubcf2026_en13'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from ubcf import routes, models