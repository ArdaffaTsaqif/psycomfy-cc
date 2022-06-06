from tkinter import E
from flask import Blueprint, jsonify
from utils import write, read, token_required
import tensorflow as tf
import json
import re
import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'psycomfyFireStorage.json'

pred = Blueprint('pred',__name__)

bucket_name = 'c22-ps203-capstone-352016.appspot.com'
bucket_folder = 'records/'
temp_folder = '/tmp/read.wav'

data_json_depresi = {}


def model_pred():
    model = tf.keras.models.load_model('model.h5')
    return model
 
#download audio from GCS to tmp
def get_audio(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(bucket_folder + filename)
    blob = blob.download_to_filename(temp_folder)
    report_id = re.sub(r"\.\w*", "", filename)
    audio_url = bucket_name+bucket_folder+filename
    data_json_depresi.update({"id":report_id, "url":audio_url})

    return data_json_depresi


#split audio from librosa load
def split_audio(audioData):

    pass

#extract feature
def features(signal):

    pass

#get prediction results
def get_predictions(features):
    
    pass

#show results
def post_predictions(data_json):
    try:
        
        pass
    except Exception as e:
        print (e)

#this endpoint will make prediction result
@pred.route('/<filename>')
def predictions(filename):
    pass

#post prediction results
@pred.route('/reports/<reports_id>')
def getResults(reports_id):
    report = read("""
        SELECT * FROM reports WHERE reports_id = %s
    """, (reports_id,))
    return jsonify(report)
