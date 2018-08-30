'''Cleans data for further use'''
import pandas as pd
import time
from datetime import datetime


def convert_to_int(string):
    '''Converts given string to an integer if needed'''
    if type(string) is str:
        return string.replace(',', '')
    return string


def convert_to_timestamp(string):
    '''Converts given string to unix time if string is given in this format:
        "January 1, 1970"'''
    return int(time.mktime(datetime.strptime(string, "%b %d, %Y").timetuple()))


df = pd.read_csv("data/data_raw.csv", index_col=0)

df['open'] = df['open'].apply(convert_to_int)
df['high'] = df['high'].apply(convert_to_int)
df['low'] = df['low'].apply(convert_to_int)
df['adj_close'] = df['adj_close'].apply(convert_to_int)
df['volume'] = df['volume'].apply(convert_to_int)
df['timestamp'] = df['date'].apply(convert_to_timestamp)

df = df[['timestamp', 'stock', 'open', 'high', 'low', 'adj_close', 'volume']]

df.to_csv("data/data_cleaned.csv")
