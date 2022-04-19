import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt

# warnings.filterwarnings("ignore")
# plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
from pandas_datareader import data as web


def getStockData(name, startDate, endDate):
    stock2 = (web.DataReader(name, data_source="yahoo", start=startDate, end=endDate))[
        "Close"
    ]
    stock2 = pd.DataFrame(stock2)
    stock2 = stock2.sort_values("Date")
    type(stock2)

    stock2.isnull().sum()
    stock2 = stock2.groupby("Date")["Close"].sum().reset_index()
    stock2
    stock2.head()

    stock2.Date = pd.to_datetime(stock2.Date, format="%Y%m%d", errors="ignore")
    stock2 = stock2.set_index("Date")
    stock2.index = pd.to_datetime(stock2.index)

    return pd.DataFrame(stock2.Close.resample("M").mean())


def getMultipleStocks(stocks, startDate, endDate):
    prices = pd.DataFrame()

    for stock in stocks:
        temp = getStockData(stock, startDate, endDate)
        prices = pd.concat([prices, temp], axis=1).reindex(temp.index)
    prices.columns = stocks
    return prices
