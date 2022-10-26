import pandas as pd
import os
import feature_extractor
import warnings
warnings.filterwarnings('ignore')

files_list = os.listdir('static/songs')

df = pd.read_csv('assets/df_100_songs.csv')

for i in range(len(files_list)):
    try:
        data = feature_extractor.audio_feature_extractor('static/songs/' + files_list[i])
        df = df.append(data, ignore_index = True)
        print('Filename:', files_list[i])
        print('Features:', data)
        print('=======================')
    except:
        print('Error for file', list_files[i])
    finally:
        df['filename'] = files_list
        fc = df.pop('filename')
        df.insert(0, 'filename', fc)
        df.to_csv('assets/df_100_songs.csv', index = False)

print(df.head(10))
