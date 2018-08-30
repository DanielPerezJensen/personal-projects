# financial-data-scrape
##### A tool for scraping financial data of any given stock from investopedia.com
##### Requirements: Python3.6

Put all stocks you want in your resulting *data_processed.csv* into the file: *stocks_list.txt*, with a new-line separating stocks. 
After adding your stocks, run: *python scrape.py*

The resulting **data_processed.csv** will look like *this*:


,  timestamp, stock, open,  high,  low,   adj_close,volume
0, 964994400, REGN,  24.88, 29.13, 24.66, 28.06,114600
1, 965080800, REGN,  28.06, 29.75, 27.0,  28.56,98200
2, 965167200, REGN,  27.75, 28.5,  26.63, 28.44,48400

