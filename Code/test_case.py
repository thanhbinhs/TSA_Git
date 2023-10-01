from vnstock import *
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter, AutoDateLocator

fpt = stock_historical_data("FPT", "2013-01-01", "2023-09-29", "1D", 'stock')
vic = stock_historical_data("VIC", "2013-01-01", "2023-09-29", "1D", 'stock')

fpt['time'] = pd.to_datetime(fpt['time'])


fpt['open'] = fpt['open'].astype(float)
vic['open'] = vic['open'].astype(float)

fig,ax1 = plt.subplots(figsize=(12,6))
plot1 = ax1.plot(fpt['time'], fpt['open'], color='red', label='FPT')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price Open FPT')
ax1.legend(loc='upper left')

ax2 = plt.subplot()
plot2 = ax2.plot(fpt['time'], vic['open'], color='blue', label='VIC')
ax2.set_ylabel('Price Open VIC')
ax2.legend(loc='upper right')

ax1.grid(True, linestyle='--', alpha=0.6)


ax1.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
for label in ax1.get_xticklabels():
    label.set_rotation(45)

plt.tight_layout()
plt.show()