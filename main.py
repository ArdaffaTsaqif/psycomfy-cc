from flask import Flask
from flask_mysqldb import MySQL
from setup import MYSQL_DB,MYSQL_PASSWORD, MYSQL_UNIX_SOCKET,MYSQL_USER


app = Flask(__name__)


app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "ardaffa123"
app.config["MYSQL_DB"] = "flaskapp"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_UNIX_SOCKET"] = "/cloudsql/c22-ps203-capstone-352016:asia-southeast2:psycomfy-demo" 
#connect 


db = MySQL(app)
 
@app.route('/')
def hello():
    return 'hello world'

from authentication import auth
app.register_blueprint(auth)