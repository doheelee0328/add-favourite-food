import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bdzmzmsh:4uTi9Dh-sMky0_ROhYjzsgWWJMJE-JVT@lucky.db.elephantsql.com/bdzmzmsh'


db = SQLAlchemy(app)


from application import models
from application import routes

if __name__ == '__main__':
    app.run(debug=True)