# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from app.routes import api

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# app.register_blueprint(api, url_prefix='/api')

# @app.route('/')
# def home():
#     return ''

# if __name__ == '__main__':
#     app.run(port=5555)
from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555)
