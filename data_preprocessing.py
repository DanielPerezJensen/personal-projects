import pandas as pd


df = pd.read_csv("data/data_cleaned.csv", index_col=0)

# list of stucks that have all datapoints
stocks_list = ['ATVI', 'ADBE', 'ALXN', 'ALGN', 'GOOG', 'GOOGL', 'AMZN', 'AAL',
               'AMGN', 'ADI', 'AAPL', 'AMAT', 'ASML', 'ADSK', 'ADP', 'BIDU',
               'BIIB', 'BMRN', 'BKNG', 'AVGO', 'CA', 'CDNS', 'CELG', 'CERN',
               'CHTR', 'CHKP', 'CTAS', 'CSCO', 'CTXS', 'CTSH', 'CMCSA', 'COST',
               'CSX', 'CTRP', 'XRAY', 'DLTR', 'EBAY', 'EA', 'EXPE', 'ESRX',
               'FB', 'FAST', 'FISV', 'GILD', 'HAS', 'HSIC', 'HOLX', 'IDXX',
               'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JBHT', 'JD', 'KLAC',
               'LRCX', 'LBTYA', 'LBTYK', 'MAR', 'MXIM', 'MELI', 'MCHP', 'MU',
               'MSFT', 'MDLZ', 'MNST', 'MYL', 'NTES', 'NFLX', 'NVDA', 'ORLY',
               'PCAR', 'PAYX', 'PYPL', 'PEP', 'QCOM', 'QRTEA', 'REGN', 'ROST',
               'STX', 'SHPG', 'SIRI', 'SWKS', 'SBUX', 'SYMC', 'SNPS', 'TMUS',
               'TTWO', 'TSLA', 'TXN', 'KHC', 'FOX', 'FOXA', 'ULTA', 'VRSK',
               'VRTX', 'VOD', 'WBA', 'WDC', 'WDAY', 'WYNN', 'XLNX']

result_df = pd.DataFrame()

for stock in stocks_list:
    stock_df = df.loc[df['stock'] == stock]
    # only append to dataframe if there is no lack of data in the date-range
    if len(stock_df) == 4530:
        stock_df = stock_df.iloc[::-1]
        result_df = result_df.append(stock_df)

result_df = result_df.reset_index(drop=True)
result_df.to_csv("data/data_processed.csv")
