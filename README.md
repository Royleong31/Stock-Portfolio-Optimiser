# Stock Portfolio Optimiser

- pyportfolio/portfolioCreator.ipynb can create 2 types of portfolios, max sharpe and min volatility
- Pyportfolio library is used to create the porfolios
- Data is taken from yahoo stock API and cleaned from there
- Portfolio is created using data from 2009-2016 and tested from 2017-2018
- Data is created and stored in csv files in pyportfolio folder
- Sharpe ratio and absolute returns are calculated for the testing and training time periods
- ARIMA part uses the csv files created to generate the predicted values.

## TO-DO
- Figure out how the ARIMA code works and optimise it
- Code is very messy. Refactor it
- Balance user input based on industry. Right now it doesn't accept user input as it just uses a fixed portfolio
- Check the calculations

## Presentation flow: 
MOTIVATION: 
- Problem statement (Which model can create a portfolio that maximizes the profit? + How can we modify other parameters (re-create period) to maximize the profit? ) 
- Data set (Stocks of 5 different industries) 

SET THE STAGE: 
- Method: 
    - Predict the stock's price using ARIMA 
    - Tryout different allocation models (pyportfolio, Sharpe ratio, Roy ratio) 
    - Make separate files to method for more flexibility 
- Data preparation:  
    - Taken from Yahoo?
    - Take only “Close” value 
    - Index the dates 
    - Take mean value of stocks in each month for clearer comparisons and  
- Exploratory analysis: 
    - The trends of all stocks 
    - The correlation between stocks 
    - Trends in industry? 
    - Other graphs 

CORE ANALYSIS: 
    - ARIMA explain (Stability and normality proof + pdqS allocation explanation) 
    - Roy ratio explain (The formula + Validity)
    - Compare the results 

FINISH: 
    - Which was the best (formula + timeframe)
    - Comment on how to expand dataset 
