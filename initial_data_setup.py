from sklearn.model_selection import train_test_split
import pandas as pd

def create_dataframe(path):
    df = pd.read_csv(path)
    return df

def column_names(dataframe, cols):
    dataframe.columns = cols
    return dataframe

def train_test_val_split(dataframe):
    train, test = train_test_split(dataframe, train_size=0.9)
    train, val = train_test_split(train, train_size=0.8)
    return train, val, test

def create_X_y(train, val, test, target):
    X_train = train.drop(target, axis=1)
    y_train = train[target]
    X_val = val.drop(target, axis=1)
    y_val = val[target]
    X_test = test.drop(target, axis=1)
    y_test = test[target]
    return X_train, y_train, X_val, y_val, X_test, y_test