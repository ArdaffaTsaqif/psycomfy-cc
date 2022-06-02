from setup import SECRET_KEY
from flask_mysqldb import MySQLdb
from main import db
from functools import wraps
from flask import request, jsonify
import jwt

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'Authorization' in request.headers:
           token = request.headers['Authorization']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
       except:
           return jsonify({'message': 'token is invalid'})
 
       return f(*args, **kwargs)
   return decorator


def read(query, params=None):
    cursor = db.connection.cursor()
    if params:
        cursor.execute(query, params)
    else :
        cursor.execute(query)

    results = cursor.fetchall()
    cursor.close()

    data = []

    for result in results:
        data.append(result)
    
    return data

def write(query, params):
    cursor = db.connection.cursor()
    try :
        cursor.execute(query, params)
        db.connection.commit()
        cursor.close()
        
        return True
    except MySQLdb._exceptions.IntegrityError:
        cursor.close()
        return False

