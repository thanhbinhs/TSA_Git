import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Sample data with a date column
data = {'date': ['2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04'],
        'value': [10, 15, 12, 18]}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Convert the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'])

# Create a plot
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the data
ax.plot(df['date'], df['value'], marker='o', linestyle='-')

# Customize the x-axis date format
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y/%m/%d'))

# Optionally, rotate the x-axis labels to avoid overlapping
plt.xticks(rotation=45)

# Set labels for x and y axes
ax.set_xlabel('Date')
ax.set_ylabel('Value')

# Draw vertical and horizontal reference lines (x=0 and y=0)
ax.axvline(x=datetime(2023, 9, 1), color='red', linestyle='--', label='x=0 (Oy)')
ax.axhline(y=0, color='blue', linestyle='--', label='y=0 (Ox)')

# Add a legend to the plot
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
