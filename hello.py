from flask import Flask, render_template, request
import requests
import base64
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=['GET', 'POST'])
def search():
    filePath = request.form["path"]
    file_contents = filePath.split(",")
    searchUrl = 'http://www.google.com/searchbyimage/upload'
    # multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    image_result = open('baseimage.jpg', 'wb')
    image_result.write(base64.b64decode(file_contents[1]))
    multipart = {'encoded_image': (filePath, open("baseimage.jpg", 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    os.remove("baseimage.jpg")
    return fetchUrl