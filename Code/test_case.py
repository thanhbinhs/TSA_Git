import pandas as pd

df = pd.read_csv("../Data/Stock/AAPL.csv")

df = df.replace('\$', '', regex=True)


df.to_csv("../Data/Stock/AAPL.csv", index=False)