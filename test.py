import urllib.request

req_url = urllib.request.urlopen("https://storage.googleapis.com/c22-ps203-capstone-352016.appspot.com/records/Houkai.3rd.full.3442464.jpg")
print(req_url.read())