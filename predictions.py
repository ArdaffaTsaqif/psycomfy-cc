from flask import Blueprint, jsonify, request
from utils import write, read, token_required
from werkzeug.utils import secure_filename
#import tensorflow as tf
import librosa
import json
import re
import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-key-googlecloud.json'

pred = Blueprint('pred',__name__)

bucket_name = 'psycomfy-c22-ps203-capstone'
temp_folder = '/tmp/'

def download_file(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(filename)
    blob = blob.download_to_filename(temp_folder + filename)

# /uploads endpoint upload audio file to GCS
@pred.route('/uploads', methods=['POST'])
@token_required
def upload_file():
    if request.files:

        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('/tmp/', filename))

        try:
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(filename)
            blob = blob.upload_from_filename('/tmp/' + filename)
            os.remove('/tmp/' + filename)
            return jsonify('success')
        except:
            return jsonify('error')
    return jsonify('error'), 401 

# /<filename> trugger by GCS
# masih development
# for running prediction
@pred.route('/<filename>')
@token_required
def tester2(filename):
    download_file(filename)
    os.remove('/tmp/'+filename)
    return jsonify({'message' : 'success'})
