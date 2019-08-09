import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")

start_date = dt.datetime(2000,1,1)
end_date = dt.datetime(2016,1,1)

df = web.DataReader('AAPL','yahoo',start_date,end_date)

print(df.head())