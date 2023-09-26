import pandas as pd
import matplotlib.pyplot as plt


path = "../Data/Stock/AAPL.csv"
path2 = "../Data/Stock/AMZN.csv"

df = pd.read_csv(path)

df = pd.DataFrame(df)

rgba_color = (0.3,0.3,0.3,0.3)

# Chuyển cột 'Date' thành datetime
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by=['Date'])
# Loại bỏ dấu $ và chuyển đổi cột giá thành float
df['Open'] = df['Open'].astype(float)
df['Volume'] = df['Volume'].astype(float)
df['Close'] = df['Close'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)
df_head = df.tail(100)
print(df_head)
df_head = df_head.sort_values(by=['Date'])

open = df_head['Open']
date = df_head['Date']
close = df_head['Close']
volume = df_head['Volume']
high = df_head['High']
low = df_head['Low']

avg = high - low

ax1 = plt.subplot()

plt1 = ax1.plot(date,close, color='red', label='Close')
ax1.set_ylabel('Avg', color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax1.set_xlabel('Date')
ax1.set_xticks([])
ax1.set_title('AMZN Stock Price')


ax2 = ax1.twinx()
bar1 = ax2.bar(date, volume, color=rgba_color, label='Volume')
ax2.set_ylabel('Volume', color=rgba_color)
ax2.tick_params(axis='y', labelcolor='green')

plt.savefig('AAPL.svg')
plt.close()

