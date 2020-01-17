import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def null_check(dataframe):
    series = dataframe.isnull().any()
    null_columns = pd.DataFrame(series, columns=['Nulls'])
    null = False
    for i in range(len(null_columns)):
        if null_columns['Nulls'].iloc[i] == True:
            print('Column', '"', null_columns.index[i], '"', 'contains null values')
            null = True
    if null == False:
        print('Your dataframe contains no null values')

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


def parse_dates(dataframe, date_column):
    """Parse an ISO-8601 formatted time stamp."""
    pd.options.mode.chained_assignment = None

    dataframe['year'] = np.NaN
    dataframe['month'] = np.NaN
    dataframe['day'] = np.NaN
    dataframe['hour'] = np.NaN
    dataframe['minute'] = np.NaN
    dataframe['second'] = np.NaN
    for i in range(len(dataframe)):
        timestamp = dataframe[date_column].iloc[i]
        year = timestamp[0:4]
        month = timestamp[5:7]
        day = timestamp[8:10]

        year = int(year)
        month = int(month)
        day = int(day)

        if (timestamp[4] != '-') | (timestamp[7] != '-'):
            raise ValueError('Invalid date separator')

        error_test = timestamp.replace(':', '')
        error_test = error_test.replace('-', '')
        error_test = error_test.replace('T', '')

        if error_test.isdigit() == False:
            raise ValueError('Not a valid datetime string')
        elif len(error_test) < 8:
            raise ValueError('Not a valid datetime string')

        if month > 12:
            raise ValueError('Not a valid month')
        if day > 31:
            raise ValueError('Not a valid day')

        if 'T' in timestamp:
            if len(timestamp) >= 13:
                hour = int(timestamp[11:13])
                hour = int(hour)
                if hour > 23:
                    raise ValueError('Not a valid hour')
                if len(timestamp) == 13:
                    dataframe['year'].iloc[i] = year
                    dataframe['month'].iloc[i] = month
                    dataframe['day'].iloc[i] = day
                    dataframe['hour'].iloc[i] = hour
            elif timestamp[13] != ':':
                raise ValueError('Invalid time separator')
            if len(timestamp) >= 16:
                minute = int(timestamp[14:16])
                minute = int(minute)
                if minute > 59:
                    raise ValueError('Not a valid minute')
                if len(timestamp) == 16:
                    dataframe['year'].iloc[i] = year
                    dataframe['month'].iloc[i] = month
                    dataframe['day'].iloc[i] = day
                    dataframe['hour'].iloc[i] = hour
                    dataframe['minute'].iloc[i] = minute
                elif timestamp[16] != ':':
                    raise ValueError('Invalid time separator')
            if len(timestamp) >= 19:
                second = int(timestamp[17:19])
                second = int(second)
                if second > 59:
                    raise ValueError('Not a valid second')
                if len(timestamp) == 19:
                    dataframe['year'].iloc[i] = year
                    dataframe['month'].iloc[i] = month
                    dataframe['day'].iloc[i] = day
                    dataframe['hour'].iloc[i] = hour
                    dataframe['minute'].iloc[i] = minute
                    dataframe['second'].iloc[i] = second
        else:
            dataframe['year'].iloc[i] = year
            dataframe['month'].iloc[i] = month
            dataframe['day'].iloc[i] = day
    date_cols = ['year', 'month', 'day', 'hour', 'minute', 'second']
    for item in date_cols:
        if dataframe[item].isnull().all():
            dataframe = dataframe.drop(item, axis=1)
        else:
            dataframe[item] = dataframe[item].astype(int)



