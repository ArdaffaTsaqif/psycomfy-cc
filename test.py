import os
from google.cloud import storage
import librosa


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'psycomfyFireStorage.json'

bucket_name = 'psycomfy-c22-ps203-capstone'
bucket_folder = 'records/'
temp_folder = '/tmp/read.wav'
def download_file(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(filename)
    blob = blob.download_to_filename(temp_folder)

download_file('ss1.png')


