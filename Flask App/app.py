import os
import pickle
import lightgbm
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import sklearn
from sklearn.preprocessing import MinMaxScaler
import feature_extractor
import preprocessing
import get_recommendations
import joblib
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads_folder/'

class_names = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
genre = [None]

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

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    percent = '%'
    
    features_dictionary = feature_extractor.audio_feature_extractor('uploads_folder/uploaded_audio_file.wav')
    X = preprocessing.preprocessor(features_dictionary, joblib.load('assets/standard_scaler.save'))

    model = pickle.load(open('assets/opt_lgbm_model.pkl', 'rb'))

    final_class = class_names[(model.predict(X.reshape(1, -1)))[0]].title()
    probs = round((max((model.predict_proba(X.reshape(1, -1)))[0]) * 100), 3)
    genre[0] = final_class

    return render_template('index.html', **locals())

@app.route('/redirect')
@app.route('/recommend', methods = ['GET', 'POST'])
def recommend():
    rec_songs = get_recommendations.generate_song_recommendations('uploaded_audio_file.wav')
    rec_songs = (rec_songs[rec_songs.label == genre[0].lower()]).head(3)

    song_names = []
    song_cosine_sim = []

    for sn in rec_songs['filename']:
        song_names.append(sn.split('.m4a', 1)[0])

    for scs in rec_songs['cosine_sim_score']:
        song_cosine_sim.append(round(scs * 100, 3))
        
    return render_template('recommendations.html', **locals()) 

if __name__ == '__main__':
    app.run(debug = True, port = 2000)