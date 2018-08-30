from bs4 import BeautifulSoup
import requests
import pandas as pd


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
               'VRTX', 'VOD', 'WBA', 'WDC', 'WDAY', 'WYNN', 'XLNX', 'S&P']

data_points = []

for stock in stocks_list:

    url = 'https://www.investopedia.com/markets/api/partial/historical/?Symbol={}&Type=%20Historical+Prices&Timeframe=Daily&StartDate=Jul+31%2C+2000&EndDate=Jul+31%2C+2018'.format(stock)
    request = requests.get(url)
    data = request.text
    soup = BeautifulSoup(data, features="html5lib")
    table = soup.find("table")

    for table_row in table.select('tr'):
        cells = table_row.findAll('td')
        if len(cells) == 6:
            date = cells[0].text.strip()
            open_val = cells[1].text.strip()
            high_val = cells[2].text.strip()
            low_val = cells[3].text.strip()
            adj_close = cells[4].text.strip()
            volume = cells[5].text.strip()
            data_points.append((stock, date, open_val, high_val, low_val,
                                adj_close, volume))
    print(stock)

data_frame = pd.DataFrame(data_points, columns=['stock', 'date', 'open',
                                                'high', 'low', 'adj_close',
                                                'volume'])
print(len(data_frame))
print(data_frame.head())

data_frame.to_csv("data/data_raw.csv")
