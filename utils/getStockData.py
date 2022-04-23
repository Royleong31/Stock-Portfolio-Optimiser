import warnings
import itertools
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pandas_datareader import data as web


def getStockData(name, startDate, endDate):
    # Only take the columns we need ("Date" and  "Close")
    stock = (web.DataReader(name, data_source="yahoo", start=startDate, end=endDate))[
        "Close"
    ]
    stock = pd.DataFrame(stock)
    stock = stock.sort_values("Date")
    type(stock)

    # Check for missing value
    stock.isnull().sum()

    # Indexing the data by date for future use
    stock = stock.groupby("Date")["Close"].sum().reset_index()
    stock.Date = pd.to_datetime(stock.Date, format="%Y%m%d", errors="ignore")
    stock = stock.set_index("Date")
    stock.index = pd.to_datetime(stock.index)

    # Resample the stock by Monthly mean value for smoother plot and better prediction
    return pd.DataFrame(stock.Close.resample("M").mean())


def getMultipleStocks(stocks, startDate, endDate):
    prices = pd.DataFrame()

    for stock in stocks:
        temp = getStockData(stock, startDate, endDate)
        prices = pd.concat([prices, temp], axis=1).reindex(temp.index)
    prices.columns = stocks
    return prices
