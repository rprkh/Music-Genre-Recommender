from flask import Flask, render_template, request
import os
import pickle
import lightgbm
import librosa

UPLOAD_FOLDER = 'upload_folder'
ALLOWED_EXTENSIONS = {'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = pickle.load(open('assets/opt_lgbm_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    audio_file = request.form['audio_file']
    result = ''

    if(audio_file.endswith('.wav') == False):
        error_message = 'Upload only a .wav file'
        result = 'Cannot predict genre due to incorrect file upload'

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug = True)