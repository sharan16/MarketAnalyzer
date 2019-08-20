import numpy as np
import pandas as pd
import pickle

def normalize_data_for_labels(tkr):
    hm_days = 7
    df = pd.read_csv('sp500data.csv',index_col = 0)
    tkrs = df.columns.values.tolist()
    df.fillna(0,inplace = True)

    for i in range(1,hm_days + 1):
        df['{}_{}d'.format(tkr,i)] =  (df[tkr]- df[tkr].shift(i))/df[tkr].shift(i)
    df.fillna(0,inplace=True)

    print(df['AAPL_2d'].head(10))
    print(df['AAPL'].head(10))

normalize_data_for_labels('AAPL')