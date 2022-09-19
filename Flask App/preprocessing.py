import pandas as pd

def preprocessor(data, scaler):
    df = pd.DataFrame([data])
    X = df.values
    X = scaler.transform(X)

    return X
