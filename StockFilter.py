import pandas as pd

nasdaq = pd.read_csv("nasdaq_stocks_list.csv")

us_companies = nasdaq[nasdaq['Country'] == "United States"].reset_index(drop=True)

symbols = us_companies["Symbol"].str.lower().to_list()