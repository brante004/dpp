import matplotlib.pyplot as plt
import pandas as pd
import datetime
from matplotlib.patches import Patch

# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present.  Create a line plot, with vertical
# lines to mark recessions:
#   March 2001 - November 2001
#   December 2007 - June 2009
#   March 2020 - January 2021 (technically not billed a recession but we'll include it anyway!)

df = pd.read_csv(r'D:\Python\dpp\unrate.csv', parse_dates=['DATE'])
df.info()

recessions = [(datetime.datetime(2001, 3, 1),  datetime.datetime(2001, 11, 1)),
              (datetime.datetime(2007, 12, 1), datetime.datetime(2009, 6, 1)),
              (datetime.datetime(2020, 3, 1),  datetime.datetime(2021, 4, 1))]
labels = 'Asian Financial Crisis', 'Sub Prime Debt Crisis', 'Covid Crisis']
legend_elements = [Patch(facecolor='grey', label=labels[0]), Patch(facecolor='grey', label=labels[1]), Patch(facecolor='grey', label=labels[2])] 

fig, ax = plt.subplots()
ax.plot(df['DATE'], df['UNRATE'], label='Unemployment Rate', color='black', marker='o', markerfacecolor='black', markersize=2)
ax.set_title('Unemployment Rate since 2000 and Major Recessions')
ax.set_xlabel('Year')
ax.set_ylabel('Unemployment Rate %')
ax.legend(loc='best')
for i in range(len(recessions)):
    ax.axvspan(recessions[i][0], recessions[i][1], color='grey', alpha=0.2)

plt.show()



