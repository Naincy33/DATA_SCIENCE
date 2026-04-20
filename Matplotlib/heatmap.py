import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

# Create Total column
df["Total"] = df["Maths"] + df["Physics"] + df["Chemistry"]

# Scatter plot
sns.scatterplot(x="Hours_Studied", y="Total", data=df)
plt.title("Study vs Marks")
plt.show()

# Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()