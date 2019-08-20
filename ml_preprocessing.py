import numpy as np
import pandas as pd
import pickle
from collections import Counter
def normalize_data_for_labels(tkr):
    hm_days = 7
    df = pd.read_csv('sp500data.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)
    for i in range(1, hm_days+1):
        df['{}_{}d'.format(tkr, i)] = (df[tkr].shift(-i) - df[tkr]) / df[tkr]
    df.fillna(0, inplace=True)
    return tickers, df

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0
def extract_feature_sets(tkr):
    tkrs, df =  normalize_data_for_labels(tkr)

    df['{}_target'.format(tkr)] = list(map(buy_sell_hold,
    df['{}_1d'.format(tkr)],
    df['{}_2d'.format(tkr)],
    df['{}_3d'.format(tkr)],
    df['{}_4d'.format(tkr)],
    df['{}_5d'.format(tkr)],
    df['{}_6d'.format(tkr)],
    df['{}_7d'.format(tkr)]
    ))
    # print(df.head())
    vals = df['{}_target'.format(tkr)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread',Counter(str_vals))
    df.fillna(0, inplace = True)
    df = df.replace([np.inf,-np.inf],np.nan)
    df.dropna(inplace = True)
    
    df_vals = df[[ticker for ticker in tkrs]].pct_change()
    df_vals = df_vals.replace([np.inf,-np.inf],0)
    df_vals.fillna(0,inplace= True)
    # print(df_vals.head())
    X = df_vals.values
    y = df['{}_target'.format(tkr)].values
    
    return X,y,df

X,y,df = extract_feature_sets('AAPL')
# print(df.head())