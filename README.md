# Stock Portfolio Optimiser

## Problem Statement
It is very difficult to predict stock prices, and most stock traders earn returns that are far below that of a control portfolio. As such, we want to use Machine Learning to help us to make better trading decisions and outperform the market.

## Data Preparation
We obtained data from the Yahoo Stock API. We obtained raw prices for all the stocks from June 2010 to March 2022. From there, we calculated the mean price for each month and trained and tested our models based on the monthly average prices. We used 13 different stocks from 5 different industries to create a diversified portfolio.

Training timeframe: June 2010 - December 2017
Testing timeframe: January 2018 - March 2022

## Exploratory Data Analysis
We plotted time series graphs to show how the stock prices change over time. As portfolio creating depends more on changing rate than the actual price, we normalised the stock prices by scaling them to the same starting point to create a fair comparison of prices.

Using the Roy Ratio, stocks that have higher correlation will have a higher chance of appearing in the same portfolio. So we will first check the correlation within each of the 5 industries to see if we should invest more in a particular industry, Later, we plot a heatmap of all chosen stocks to see if there are stocks in different industries that may appear together.

We will also go into analyze one of the stocks as time series to have more insight about the stock. We will also conduct necessary steps here to demonstrate how can we preprocess the dataset before get it ready for forecasting value.


//May delete these
We used stocks from different industries to reduce the correlation between the stocks so that when the stock prices of 1 industry falls, it can be countered by an increase in the stock prices of other industries. As such, we plotted the correlation heatmaps of all the stocks to see how correlated the stocks are to each other. 


## Machine Learning Techniques
We will predict future values using ARIMA model.
The steps including:
- Preprocessing (differencing to stationarize the datasets)
- Define p, d, q value for each of the stocks' predicting process using AIC score
- Apply ARIMA to predict next point value
- After each prediction, used predicted value for future forecasting
- Upon reaching the end date desired, conduct diagnosis and analysis for the values predicted
- Back checking and calculate the actual return using ARIMA model and Roy Ratio



@lakshya-aga
- PLEASE HELP TO FILL IN

## Outcome
Besides creating the ARIMA based portfolio, we also created 2 control portfolios to compare the our model against. Both controls started with the same 1/13 value allocation for each stock. 1 of these control portfolios used a buy and hold strategy while the other was rebalanced back to the same portfolio allocation monthly.
We compared the returns of the 3 portfolios and found that our portfolio not only returned the best absolute returns, but also the best risk adjusted returns, showing that it is the potentially most effective portfolio.

## What we learnt
Time series data was not covered in the course syllabus, so analysing time series data and building an ARIMA was something new to us. We learnt about how statistics affected the parameters that go into creating the ARIMA model and how we can use graphs to find the best parameters. We also learnt how to write scripts to create the portfolios because we needed to manipulate the raw stock price data into useful data that can be used for portfolio analysis. In terms of data visualisation, we learnt that plotting raw stock prices of each stock against time would give a misleading graph because different stocks have different starting stock prices, so plotting a simple graph of price against time would create a graph that is skewed towards stocks with higher prices. So we learnt that in order to create an accurate representation, normalisation of the data is necessary.

- INPUT MORE HERE
