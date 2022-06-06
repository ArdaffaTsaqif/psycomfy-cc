import os
from google.cloud import storage
import librosa


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'psycomfyFireStorage.json'

bucket_name = 'c22-ps203-capstone-352016.appspot.com'
bucket_folder = 'records/'
temp_folder = '/tmp/read.wav'
def download_file(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(bucket_folder + filename)
    blob = blob.download_to_filename(temp_folder)

download_file('record1.wav')



y, sr = librosa.load(temp_folder)
print(y)
os.remove(temp_folder)
