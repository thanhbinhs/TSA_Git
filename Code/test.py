import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.dates import DateFormatter, AutoDateLocator


# Read in the data
path = '../Data/AAPL.csv'

df = pd.read_csv(path)

df['Date'] = pd.to_datetime(df['Date'])
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)


date = df['Date']
open = df['Open']
close = df['Close']
high = df['High']
low = df['Low']

# Plotting again with correct date labels and adjusted rotation
fig, ax1 = plt.subplots(figsize=(12,6))

plot1 = ax1.plot(date, open, color='red', label='Open')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price Open')
ax1.set_title('Price Open and Close')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
plot2 = ax2.plot(date, close, color='blue', label='Close')
ax2.set_ylabel('Price Close')
ax2.legend(loc='upper right')

ax1.grid(True, linestyle='--', alpha=0.6)

# Use Locator to fix the number of ticks on the x-axis
locator = AutoDateLocator(maxticks=10)
ax1.xaxis.set_major_locator(locator)

# Format the x-axis label and set rotation
ax1.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
for label in ax1.get_xticklabels():
    label.set_rotation(70)

plt.tight_layout()
plt.show()
