import pandas as pd
data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 35]
]
 
df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)

#using numpy

import numpy as np

arr = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(arr, columns=["A", "B"])
print(df)