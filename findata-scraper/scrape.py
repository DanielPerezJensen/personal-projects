from data_get import data_get
from data_clean import data_clean
from data_preprocessing import data_preprocessing


stocks_list = []
with open("stocks_list.txt", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
    stocks_list.extend(data)

# data_get(stocks_list)
data_clean()
data_preprocessing()
