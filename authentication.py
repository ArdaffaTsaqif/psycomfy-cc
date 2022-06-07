from flask import Blueprint, jsonify, request
from utils import read, write
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import re
import jwt
from setup import SECRET_KEY
from utils import token_required

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=['POST'])
def add_user():
    entries = request.form
    email = entries['email']
    password = entries['password']
    confirm_pass = entries['confirm_password']

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.fullmatch(regex,email) and password == confirm_pass and len(password) >= 6:
        
        hashed_pass = generate_password_hash(password, method='sha256')
        public_id = str(uuid.uuid4())

        if write("""
        INSERT INTO users (public_id, email, password) VALUES (%s, %s, %s)
    """, (public_id, email, hashed_pass)):
            return 'New user added successfully !'
        else:
            return jsonify('401')
    else:
        return jsonify('400')    

@auth.route("/signin", methods=['POST'])
def login():
    entries = request.form

    current_email = entries['email']
    current_pass = entries['password']

    current_user = read("""
        SELECT * from users WHERE email =%s
    """, (current_email,))

    if check_password_hash(current_user[0]['password'], current_pass):

        token = jwt.encode({'public_id':current_user[0]['public_id']}, SECRET_KEY, "HS256")
        return jsonify({'error' : False, 'message' : 'success','token':token})
    return jsonify({'error' : True, 'message': 'user invalid'})


@auth.route('/test')
@token_required
def test1():
    return 'success'