import pandas as pd
data = [10, 20, 30]
s = pd.Series(data)
print(s)
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

