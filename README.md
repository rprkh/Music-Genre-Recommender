# Music Genre Recognizer

Trained a Light Gradient Boosting Machine (LGBM) model to identify
10 different genres of music, with an accuracy of 90% on the test set,
an F1 score of 0.90 and an RMSE of 1.03. The model is deployed using
Flask.

Optuna was used to perform hyperparameter tuning and improve the accuracy
of the model by 8% (from 82% to 90%). Once an audio file is uploaded to the 
website by the user 58 different features
are extracted and passed to the model, to accurately identify the genre
of music.

### Dataset Used

https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

### Flask App

![Nav Bar](https://github.com/rprkh/Music-Genre-Recognizer/blob/main/Flask%20App/images/1.png)
<br>
<br>
![Nav Bar](https://github.com/rprkh/Music-Genre-Recognizer/blob/main/Flask%20App/images/2.png)

### Comparison of Different ML Models

| Machine Learning Model                                  | Test Accuracy | F1 Score | RMSE  |
| :------------------------------------------------------ | :------------ | :------- | :---- |          
| Light Gradient Boosting Machine (Optimized)             | 90%           | 0.902    | 1.034 |
| Cat Boost Classifier (Default)                          | 85%           | 0.852    | 1.746 |   
| XGBoost Classifier (Optimized)                          | 85%           | 0.849    | 1.688 |
| Random Forest Classifier (Optimized)                    | 84%           | 0.841    | 1.860 |
| Random Forest Classifier (Default)                      | 82%           | 0.827    | 1.833 |
| Gradient Boosting Classifier (Default)                  | 82%           | 0.823    | 1.612 |
| Light Gradient Boosting Machine (Default)               | 82%           | 0.818    | 1.882 |
| XGBoost Classifier (Default)                            | 81%           | 0.808    | 1.786 |
| Support Vector Classifier (Default)                     | 76%           | 0.753    | 1.939 |
| Logistic Regression (Default)                           | 73%           | 0.729    | 2.140 |
| KNN (Default)                                           | 69%           | 0.695    | 2.293 |
| Decision Tree Classifier (Default)                      | 59%           | 0.582    | 3.231 |

### Usage

Clone the repository

```bash
https://github.com/rprkh/Music-Genre-Recognizer.git
```

Install the requirements

```bash
pip install requirements.txt
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