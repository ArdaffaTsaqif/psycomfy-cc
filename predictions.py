from flask import Blueprint, jsonify
from numpy import var
from utils import write, read
import tensorflow as tf
from urllib import request
import json

pred = Blueprint('pred',__name__)

var_gcs = open("var.json")
load_var = json.load(var_gcs)
base_url = load_var['base_url']
data_json_depresi = {}

def model_pred():
    model = tf.keras.models.load_model('model.h5')
    return model
 
#download audio from GCS 
def get_audio(filename):
    
    pass

#split audio
def split_audio():
    pass

#extract feature
def features(signal):
    pass

def predictions(features):
    pass

#this endpoint will make prediction result
@pred.route('/<filename>')
def getPredictions(filename):
    pass

#post prediction results
@pred.route('/reports/<reports_id>')
def getResults(reports_id):
    report = read("""
        SELECT * FROM reports WHERE reports_id = %d
    """, (reports_id,))
    return jsonify(report)
