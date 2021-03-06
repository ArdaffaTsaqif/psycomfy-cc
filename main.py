from flask import Flask, request
import json
from flask_mysqldb import MySQL
from setup import MYSQL_DB,MYSQL_PASSWORD, MYSQL_UNIX_SOCKET,MYSQL_USER
#import pyrebase
#import firebase_admin
#from firebase_admin import credentials, auth
import sys
app = Flask(__name__)

   
app.config["MYSQL_USER"] = MYSQL_USER
app.config["MYSQL_PASSWORD"] = MYSQL_PASSWORD
app.config["MYSQL_DB"] = MYSQL_DB
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_UNIX_SOCKET"] = MYSQL_UNIX_SOCKET



db = MySQL(app)

@app.route('/')
def main():
    return 'Hello user'

from predictions import pred
app.register_blueprint(pred)

from authentications import auth
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)