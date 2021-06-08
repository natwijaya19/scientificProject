from yahoo_fin.stock_info import get_data
from datetime import datetime

#%%
endate = datetime.now()
amazon_weekly= get_data("amzn", start_date="12/04/2009", end_date=endate, index_as_date = True, interval="1wk")
print(amazon_weekly)

#%%
ticker_list = ["amzn", "aapl", "ba"]
historical_datas = {}
for ticker in ticker_list:
    historical_datas[ticker] = get_data(ticker)

print(historical_datas)


#%%
historical_datas['amzn']