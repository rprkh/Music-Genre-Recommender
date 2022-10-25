import pandas as pd
import numpy as np
import pickle
import joblib
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('assets/df_100_songs.csv')
filenames = df['filename']
df.drop(['filename'], axis = 1, inplace = True)

model = pickle.load(open('assets/opt_lgbm_model.pkl', 'rb'))
scaler = joblib.load('assets/standard_scaler.save')
class_names = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

scaled_df = scaler.transform(df)
X = scaled_df

y_pred = model.predict(X)

final_classes = []
for i in y_pred:
    final_classes.append(class_names[int(i)])

new_df = pd.DataFrame({'filename': filenames, 'label': final_classes})
new_df.to_csv('assets/classified_100_songs.csv', index = False)