import pandas as pd


def data_preprocessing():

    df = pd.read_csv("data/data_cleaned.csv", index_col=0)

    result_df = pd.DataFrame()

    for stock in list(set(df["stock"].tolist())):
        stock_df = df.loc[df["stock"] == stock]
        # only append to dataframe if there
        # is no lack of data in the date-range
        if len(stock_df) == 4530:
            stock_df = stock_df.iloc[::-1]
            result_df = result_df.append(stock_df)
        print(stock)

    result_df = result_df.reset_index(drop=True)
    result_df.to_csv("data/data_processed.csv")


if __name__ == "__main__":
    data_preprocessing()
