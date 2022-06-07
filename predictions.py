from tkinter import E
from flask import Blueprint, jsonify, request
from utils import write, read, token_required
from werkzeug.utils import secure_filename
#import tensorflow as tf
import json
import re
import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'psycomfyFireStorage.json'

pred = Blueprint('pred',__name__)

bucket_name = 'c22-ps203-capstone-352016.appspot.com'
bucket_folder = 'records/'

# /uploads endpoint upload audio file to GCS
@pred.route('/uploads', methods=['POST'])
def upload_file():
    if request.files:

        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('/tmp/', filename))

        try:
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(bucket_folder + filename)
            blob = blob.upload_from_filename('/tmp/' + filename)
            os.remove('/tmp/' + filename)
            return jsonify('success')
        except:
            return jsonify('error')
    return jsonify('error'), 401
