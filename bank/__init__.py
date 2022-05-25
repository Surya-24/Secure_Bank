from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SECRET_KEY'] = '61b3df53f0432977ca3d49e1'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
from bank import routes
def db_init(app):
    db.init_app(app)

    # Creates the tables if the db doesnt already exist
    with app.app_context():
        db.create_all()