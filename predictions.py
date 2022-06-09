from asyncore import write
from flask import Blueprint, jsonify, request
from utils import write, read, token_required
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from PIL import Image
import io, numpy as np
from io import BytesIO
import librosa
import os
import re
import cv2
from google.cloud import storage


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-key-googlecloud.json'

pred = Blueprint('pred',__name__)

bucket_name = 'psycomfy-c22-ps203-capstone'
temp_folder = '/tmp/'
base_url = ''

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

def loaded_model():
    model = tf.keras.models.load_model('predictive_model_v_8.h5')
    return model

#predict function
def predict(filename):
    download_file(filename)
    y, sr = librosa.load('/tmp/' + filename)
    librosa.feature.melspectrogram(y=y, sr=sr)
    #S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    #fig, ax = plt.subplots()
    #S_dB = librosa.power_to_db(S, ref=np.max)
    #img = librosa.display.specshow(S_dB)
    # ax.set(title='Log Mel-frequency spectrogram')
    b = BytesIO()
    plt.savefig(b, format='jpg')  #save picture in local memory
    #spectogram to numpy
    b.seek(0)
    file_bytes = np.asarray(bytearray(b.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (512, 512))
    image = image.astype("float") / 255.0
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    hasil = image
    model = loaded_model()
    y_pred = np.argmax(model.predict(hasil), axis=1)
    x_accuracy = model.predict(hasil)[0]
    output = max(x_accuracy)
    percentage = str(2*(output - 0.5)*100) + " %"
    os.remove('/tmp/'+filename)
    if str(y_pred[0]) == "0":
       label_nama = "Depresi"
       accuracy = percentage
    elif str(y_pred[0]) == "1":
       label_nama = "Normal"
       accuracy = '-'
    return label_nama, accuracy

@pred.route('/<filename>')
def start_prediction(filename):
    try:
        img = predict(filename)
        pred = {'status_user' : img[0], "status_running" : "Success", "level" : img[1]}, 201
        return pred
    except:
        pred = {'status_user' : '-', 'status_running' : "Error"}, 400
    return jsonify({'error':True, 'message':'Files input invalid'})