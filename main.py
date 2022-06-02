from flask import Flask
from flask_mysqldb import MySQL
from setup import MYSQL_DB,MYSQL_PASSWORD, MYSQL_UNIX_SOCKET,MYSQL_USER


app = Flask(__name__)
app.config['MYSQL_HOST'] = "34.101.160.253"
app.config["MYSQL_USER"] = MYSQL_USER
app.config["MYSQL_PASSWORD"] = MYSQL_PASSWORD
app.config["MYSQL_DB"] = MYSQL_DB
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_UNIX_SOCKET"] = MYSQL_UNIX_SOCKET

db = MySQL(app)
 


from authentication import auth
app.register_blueprint(auth)