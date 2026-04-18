import pandas as pd
df1 = pd.DataFrame({"ID": [1, 2]})
df2 = pd.DataFrame({"Score": [90, 80]})

print(pd.concat([df1, df2], axis=1))