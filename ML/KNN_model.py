import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier

# -------------------------
# 📂 DATASET
# -------------------------
data = {
    "Study_Hours": [1,2,3,4,5,6,7,8],
    "Sleep_Hours": [5,6,5,7,6,8,7,8],
    "Result": ["Fail","Fail","Fail","Pass","Pass","Pass","Pass","Pass"]
}

df = pd.DataFrame(data)

print(df)

# -------------------------
# 🧠 FEATURES & LABELS
# -------------------------
X = df[["Study_Hours", "Sleep_Hours"]]
y = df["Result"]

# -------------------------
# 🤖 KNN MODEL
# -------------------------
model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

# -------------------------
# 🔮 PREDICTION
# -------------------------
new_student = [[5,6]]

prediction = model.predict(new_student)

print("\nPrediction for student:", prediction)

# -------------------------
# 📊 GRAPH PLOT
# -------------------------
plt.figure(figsize=(8,5))

# Scatter plot
sns.scatterplot(
    x="Study_Hours",
    y="Sleep_Hours",
    hue="Result",
    s=120,
    data=df
)

# New point
plt.scatter(
    5, 6,
    color="black",
    s=250,
    marker="X",
    label="New Student"
)

plt.title("KNN Pattern Matching")
plt.xlabel("Study Hours")
plt.ylabel("Sleep Hours")

plt.legend()
plt.grid()

plt.show()