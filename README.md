# Music Genre Recommender

Music Genre Recommendation website that can identify and recommend 10 different genres 
of music using Light Gradient Boosting Machine (LGBM). The model achieves
an accuracy of 90% on the test set and an F1 score of 0.90. 
The training data consists of 1000 audio samples each of a duration of 
30 seconds. The model is deployed using Flask.

Optuna was used to perform hyperparameter tuning and improve the accuracy
of the model by 8% (from 82% to 90%). Once an audio file is uploaded to the 
website by the user, 58 different features are extracted and passed to the 
model to accurately identify the genre of music. Relevant song recommendations 
are generated using cosine similarity and the classified genre of music.

### Features

- Upload `.wav` files for music recognition and recommendation
- Validate the type of file uploaded to the website
- Predict the genre of music
- Get top 3 song recommendations
- Play the recommended songs on the website
- Display a loading icon while predicting and recommending songs to the user

### Dataset Used

https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

### Training and Recommendations

- Training Notebook: https://drive.google.com/file/d/1VaO11fxIl262rfSwtsvBOXP8wlhnE12n/view?usp=share_link
- Recommendation Notebook: https://drive.google.com/file/d/1q-u6jvyTLO0WuXmDJuXhKk1SMlh0EVYv/view?usp=sharing 

### Flask App


![image](https://user-images.githubusercontent.com/75483881/206853874-5aaa1e33-5503-45d7-9829-fb781ff4d0e6.png)
<br>
<br>
![image](https://user-images.githubusercontent.com/75483881/206853913-69bbf3cb-d5dd-473d-8906-ee9f3d71d9f4.png)
<br>
<br>
![image](https://user-images.githubusercontent.com/75483881/206853921-be4a84c1-df87-4d37-a092-f19781240a0d.png)

### Comparison of Different ML Models

| Machine Learning Model                                  | Test Accuracy | F1 Score |
| :------------------------------------------------------ | :------------ | :------- |         
| Light Gradient Boosting Machine (Optimized)             | 90%           | 0.902    |
| Cat Boost Classifier (Default)                          | 85%           | 0.852    |   
| XGBoost Classifier (Optimized)                          | 85%           | 0.849    |
| Random Forest Classifier (Optimized)                    | 84%           | 0.841    |
| Random Forest Classifier (Default)                      | 82%           | 0.827    |
| Gradient Boosting Classifier (Default)                  | 82%           | 0.823    |
| Light Gradient Boosting Machine (Default)               | 82%           | 0.818    |
| XGBoost Classifier (Default)                            | 81%           | 0.808    |
| Support Vector Classifier (Default)                     | 76%           | 0.753    |
| Logistic Regression (Default)                           | 73%           | 0.729    |
| KNN (Default)                                           | 69%           | 0.695    |
| Decision Tree Classifier (Default)                      | 59%           | 0.582    |

### Usage

Clone the repository

```bash
git clone https://github.com/rprkh/Music-Genre-Recognizer.git
```

Navigate to the root directory of the project

```bash
cd Music-Genre-Recognizer
```

Install the requirements

```bash
pip install -r requirements.txt
```

Navigate to the `Flask App` folder

```bash
cd "Flask App"
```

Run the `app.py` script
```bash
python app.py
```

The website should start on `http://127.0.0.1:2000/`
