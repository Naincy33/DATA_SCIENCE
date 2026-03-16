import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Aman"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

df.to_excel("students.xlsx", index=False)