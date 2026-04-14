import pandas as pd
df= pd.read_csv("data_cleaning_sample.csv")
#df = pd.read_csv("../Pandas/data_cleaning_sample.csv")
print(df)
print(df.isnull())
print(df.isnull().sum())