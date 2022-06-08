from flask import Flask
from flask_mysqldb import MySQL
from setup import MYSQL_DB,MYSQL_PASSWORD, MYSQL_UNIX_SOCKET,MYSQL_USER
import os

app = Flask(__name__)


app.config["MYSQL_USER"] = MYSQL_USER
app.config["MYSQL_PASSWORD"] = MYSQL_PASSWORD
app.config["MYSQL_DB"] = MYSQL_DB
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_UNIX_SOCKET"] = MYSQL_UNIX_SOCKET



db = MySQL(app)
 
@app.route('/')
def hello():
    return 'hello world'

from authentication import auth
app.register_blueprint(auth)

from predictions import pred
app.register_blueprint(pred)