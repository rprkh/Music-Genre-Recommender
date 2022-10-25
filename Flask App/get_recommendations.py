import feature_extractor
import pandas as pd
import numpy as np
import joblib
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

def generate_song_recommendations(song_name):
    features_dictionary = feature_extractor.audio_feature_extractor('uploads_folder/' + song_name)
    features_dictionary['filename'] = song_name

    df = pd.read_csv('assets/df_100_songs.csv')
    if(song_name in df['filename'].values):
        df = df.drop(df.index[99])
    df.loc[100] = features_dictionary

    og_df = pd.read_csv('assets/original_1000_songs.csv')
    og_df.drop(columns = ['label'], inplace = True, axis = 1)
    og_df_columns_order = og_df.columns

    df = df[[col for col in og_df_columns_order]]

    new_df = df.to_csv('assets/df_100_songs.csv', index = False)
    new_df = pd.read_csv('assets/df_100_songs.csv')

    cossim_df = new_df.iloc[:, 1:]

    similarity = cosine_similarity(cossim_df)
    df_similarity = pd.DataFrame(similarity)
    df_similarity.columns = df['filename']
    df_similarity = df_similarity.set_index(df['filename'])
    df_similarity.to_csv('assets/recommended_songs.csv')

    recommendations = df_similarity[song_name].sort_values(ascending = False)
    recommendations = recommendations.drop(song_name)
    recommendations = pd.DataFrame(recommendations).to_csv('assets/recommended_songs.csv') 
    rec_songs = pd.read_csv('assets/recommended_songs.csv')
    rec_songs.rename(columns = {'uploaded_audio_file.wav': 'cosine_sim_score'}, inplace = True)

    df_to_merge = pd.read_csv('assets/classified_100_songs.csv')
    merged_df = pd.merge(rec_songs, df_to_merge, on = 'filename', how = 'left')
    
    return merged_df