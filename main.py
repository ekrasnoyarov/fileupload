
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/downloads')
def downloads():
    return render_template('downloads.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file[]']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('file_upload.html')


@app.route('/test.txt')
def download_file():
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename='test.txt', as_attachment=True)
