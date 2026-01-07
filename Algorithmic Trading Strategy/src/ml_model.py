print("ml_model.py LOADED")

from sklearn.linear_model import LogisticRegression


def train_ml_model(df):
    """
    Trains a Logistic Regression model to predict
    next-day price direction using SMA features.
    """

    df['Future_Return'] = df['Close'].shift(-1) / df['Close'] - 1
    df['Target'] = (df['Future_Return'] > 0).astype(int)

    df = df.dropna()

    X = df[['SMA_20', 'SMA_50']]
    y = df['Target']

    model = LogisticRegression()
    model.fit(X, y)

    return model, df
