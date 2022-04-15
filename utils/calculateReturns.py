# ?: Calculates the percentage change in the value of each stock from the previous time period
def calculateReturns(portfolio):
    indexes = [i for i in range(portfolio.shape[0])]
    portfolio['indexNum'] = indexes
    portfolio = portfolio.set_index('indexNum')
    portfolioDailyChange = portfolio

    aaplDailyChange = [0]
    cahDailyChange = [0]
    cmcsaDailyChange = [0]
    dishDailyChange = [0]
    googDailyChange = [0]
    hsyDailyChange = [0]
    jnjDailyChange = [0]
    jpmDailyChange = [0]
    kDailyChange = [0]
    maDailyChange = [0]
    nflxDailyChange = [0]
    ulDailyChange = [0]
    wbaDailyChange = [0]

    for index, row in portfolioDailyChange.iterrows():
        if index==0:
            continue
        previousVal = portfolioDailyChange.iloc[[index-1]]['AAPL']
        percentageChange = (row['AAPL'] - previousVal)/previousVal*100
        aaplDailyChange.append(float(percentageChange))
        
        previousVal = portfolioDailyChange.iloc[[index-1]]['CAH']
        percentageChange = (row['CAH'] - previousVal)/previousVal*100
        cahDailyChange.append(float(percentageChange))

        previousVal = portfolioDailyChange.iloc[[index-1]]['CMCSA']
        percentageChange = (row['CMCSA'] - previousVal)/previousVal*100
        cmcsaDailyChange.append(float(percentageChange))


        previousVal = portfolioDailyChange.iloc[[index-1]]['DISH']
        percentageChange = (row['DISH'] - previousVal)/previousVal*100
        dishDailyChange.append(float(percentageChange))


        previousVal = portfolioDailyChange.iloc[[index-1]]['GOOG']
        percentageChange = (row['GOOG'] - previousVal)/previousVal*100
        googDailyChange.append(float(percentageChange))

        previousVal = portfolioDailyChange.iloc[[index-1]]['HSY']
        percentageChange = (row['HSY'] - previousVal)/previousVal*100
        hsyDailyChange.append(float(percentageChange))


        previousVal = portfolioDailyChange.iloc[[index-1]]['JNJ']
        percentageChange = (row['JNJ'] - previousVal)/previousVal*100
        jnjDailyChange.append(float(percentageChange))


        previousVal = portfolioDailyChange.iloc[[index-1]]['JPM']
        percentageChange = (row['JPM'] - previousVal)/previousVal*100
        jpmDailyChange.append(float(percentageChange))


        previousVal = portfolioDailyChange.iloc[[index-1]]['K']
        percentageChange = (row['K'] - previousVal)/previousVal*100
        kDailyChange.append(float(percentageChange))


        previousVal = portfolioDailyChange.iloc[[index-1]]['MA']
        percentageChange = (row['MA'] - previousVal)/previousVal*100
        maDailyChange.append(float(percentageChange))


        previousVal = portfolioDailyChange.iloc[[index-1]]['NFLX']
        percentageChange = (row['NFLX'] - previousVal)/previousVal*100
        nflxDailyChange.append(float(percentageChange))


        previousVal = portfolioDailyChange.iloc[[index-1]]['UL']
        percentageChange = (row['UL'] - previousVal)/previousVal*100
        ulDailyChange.append(float(percentageChange))

        
        previousVal = portfolioDailyChange.iloc[[index-1]]['WBA']
        percentageChange = (row['WBA'] - previousVal)/previousVal*100
        wbaDailyChange.append(float(percentageChange))

        

    # print(float(aaplDailyChange[1]))
    portfolioDailyChange['AAPLPercentageChange'] = aaplDailyChange
    portfolioDailyChange['CAHPercentageChange'] = cahDailyChange
    portfolioDailyChange['CMCSAPercentageChange'] = cmcsaDailyChange
    portfolioDailyChange['DISHPercentageChange'] = dishDailyChange
    portfolioDailyChange['GOOGPercentageChange'] = googDailyChange
    portfolioDailyChange['HSYPercentageChange'] = hsyDailyChange
    portfolioDailyChange['JNJPercentageChange'] = jnjDailyChange
    portfolioDailyChange['JPMPercentageChange'] = jpmDailyChange
    portfolioDailyChange['KPercentageChange'] = kDailyChange
    portfolioDailyChange['MAPercentageChange'] = maDailyChange
    portfolioDailyChange['NFLXPercentageChange'] = nflxDailyChange
    portfolioDailyChange['ULPercentageChange'] = ulDailyChange
    portfolioDailyChange['WBAPercentageChange'] = wbaDailyChange


    portfolioDailyChange = portfolioDailyChange.drop(columns=['AAPL', 'CAH', 'CMCSA', 'DISH', 'GOOG', 'HSY', 'JNJ', 'JPM', 'K', 'MA', 'NFLX', 'UL', 'WBA'])
    return portfolioDailyChange

def portfolioReturnFixedAllocation(portfolioDailyChange, stocksAllocation):
    portfolioChangesArr = []

    for index, row in portfolioDailyChange.iterrows():
        if index==0:
            continue
        portfolioChange = row['AAPLPercentageChange'] * stocksAllocation['AAPL'] + row['CAHPercentageChange'] * stocksAllocation['CAH'] +  row['CMCSAPercentageChange'] * stocksAllocation['CMCSA'] +  row['DISHPercentageChange'] * stocksAllocation['DISH'] +  row['GOOGPercentageChange'] * stocksAllocation['GOOG'] +  row['HSYPercentageChange'] * stocksAllocation['HSY'] +  row['JNJPercentageChange'] * stocksAllocation['JNJ'] +  row['JPMPercentageChange'] * stocksAllocation['JPM'] +  row['KPercentageChange'] * stocksAllocation['K'] +  row['MAPercentageChange'] * stocksAllocation['MA'] +  row['NFLXPercentageChange'] * stocksAllocation['NFLX'] +  row['ULPercentageChange'] * stocksAllocation['UL'] +  row['WBAPercentageChange'] * stocksAllocation['WBA']
        
        portfolioChangesArr.append(portfolioChange)
            # print(row['AAPLPercentageChange'])
        
    return portfolioChangesArr

def calculatePortfolioValue(portfolioChangesArr):
    cumulativeChange = 1
    portfolioValuesArr = []
    for i in portfolioChangesArr:
        cumulativeChange *= 1 + (i/100)
        portfolioValuesArr.append(cumulativeChange)
        
    return portfolioValuesArr