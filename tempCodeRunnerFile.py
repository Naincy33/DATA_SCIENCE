import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df)

print(df.head())
print(df.tail())

print(df.describe())

print(df.isnull().sum())