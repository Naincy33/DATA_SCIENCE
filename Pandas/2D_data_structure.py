import pandas as pd
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)
print(df)

df.index = ["a", "b", "c"]
df.columns = ["Name", "Age", "City"]