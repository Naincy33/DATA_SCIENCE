import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

# -------------------------
# 📂 LOAD DATA
# -------------------------
df = pd.read_csv("students_big.csv")

print(df.head())

# -------------------------
# 🧠 FEATURES & LABEL
# -------------------------
X = df[["Hours_Studied", "Sleep_Hours", "Screen_Time"]]
y = df["Result"]
# -------------------------
# 🤖 MODEL TRAIN
# -------------------------
model = DecisionTreeClassifier()
model.fit(X, y)

# -------------------------
# 🔮 PREDICTION
# -------------------------
print("\nPrediction for [4,7,3]:", model.predict([[4,7,3]]))

# -------------------------
# 📊 MULTI-GRAPH DASHBOARD
# -------------------------
fig, axs = plt.subplots(2,2, figsize=(12,8))

# 🔹 Scatter: Study vs Marks
sns.scatterplot(x="Hours_Studied", y="Marks", hue="Result", data=df, ax=axs[0,0])
axs[0,0].set_title("Study vs Marks")

# 🔹 Scatter: Screen vs Marks
sns.scatterplot(x="Screen_Time", y="Marks", hue="Result", data=df, ax=axs[0,1])
axs[0,1].set_title("Screen Time vs Marks")

# 🔹 Boxplot: Sleep vs Marks
sns.boxplot(x="Result", y="Sleep_Hours", data=df, ax=axs[1,0])
axs[1,0].set_title("Sleep vs Result")

# 🔹 Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=axs[1,1])
axs[1,1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.show()