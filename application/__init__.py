import os
import secrets
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)

app.config["SECRET_KEY"] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bdzmzmsh:4uTi9Dh-sMky0_ROhYjzsgWWJMJE-JVT@lucky.db.elephantsql.com/bdzmzmsh"

os.getenv('DATABASE_URL')

db = SQLAlchemy(app)


from application import models
from application import routes

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)