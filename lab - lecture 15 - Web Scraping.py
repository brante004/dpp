import pandas_datareader.data as web
import requests
import pandas_datareader
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#prices of Tesla (TSLA) from January 1st 2019 to December 1st 2021.

#Hint: https://www.alphavantage.co/support/#api-key

api_key = '6AFFEMKR9VZ1TQF6'
start = datetime.date(year=2019, month=1, day=1)
end = datetime.date(year=2021, month=12, day=1)
data = web.DataReader('TSLA', 'av-monthly', start=start, end=end, api_key=api_key)
data

# 2. Create a new column that holds the rolling 3 month average.

data['3ma_closing'] = data['close'].rolling(3).mean()
data

# 3. Create a new dataframe from the base data from part 1 that resamples
# the data to quarterly, using the mean value.

data.index = pd.to_datetime(data.index)
data_rs = data.resample('Q')[['close']].mean()
data_rs

# 4. Create a figure showing the time series for the monthly level and
# the monthly rolling average together.

data_rs.info()
data_rs.index
data.index

fig, ax = plt.subplots()
ax.plot(data.index, data['close'])

ax2 = ax.twinx()
ax.plot(data_rs.index, data_rs['close'])

ax.legend(loc='best')

fig.show()
