import pandas as pd
import datetime

import pandas_datareader.data as web
from pandas_datareader import wb

import requests



#fred
start = datetime.date(year=2000, month=1,  day=1)
end   = datetime.date(year=2010, month=12, day=31)
series = 'ILUR'
source = 'fred'

df = web.DataReader(series, source, start, end)
df.head()

series = ['ILUR', 'WIUR', 'MIUR']
df = web.DataReader(series, source, start, end)
df.head()

#world bank
indicator = 'NY.GDP.MKTP.CD'
country = 'CL'

df = wb.download(indicator=indicator, 
                 country=country, 
                 start=2000, end=2010)
df.head()

country = ['CL', 'AR', 'BR']
df = wb.download(indicator=indicator, 
                 country=country, 
                 start=2000, end=2010)
df.head()
df.reset_index()['country'].unique()

pd.set_option('display.float_format', lambda x: '%.2f' % x) #don't want to see that scientific notation?
df.head()
df
#requests and non-text
url = 'http://standupeconomist.com/pdf/misc/interstellar.pdf'
response = requests.get(url)
data = response.content
with open(r'c:\users\jeff levy\desktop\interstellar.pdf', 'wb') as ofile:
    ofile.write(data)

response
data
ofile

ofile = open(r'D:\Python\dpp\interstellar_test.pdf', 'wb')
ofile.write(data)
ofile.close()

ofile
