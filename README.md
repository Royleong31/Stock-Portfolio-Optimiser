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
