import os
import numpy as np
import pandas as pd
import pickle
import lightgbm
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import librosa
# import IPython.display as ipd
import sklearn
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads_folder/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for files in os.listdir(app.config['UPLOAD_FOLDER']):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], files))

        file = request.files['file']
        filename = secure_filename(file.filename)

        if(filename.endswith('.wav') == True):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.rename(os.path.join(app.config['UPLOAD_FOLDER'], filename),
                    os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_audio_file.wav'))
            message = 'File upload successful'
        else:
            message = 'Upload only .wav files'

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug = True)