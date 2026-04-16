import pandas as pd
import matplotlib.pyplot as plt

# 📂 Load dataset
df = pd.read_csv("students.csv")

# 👀 View data
print("First 5 rows:\n", df.head())

# ℹ️ Info about dataset
print("\nInfo:\n")
print(df.info())

# 📊 Basic statistics
print("\nStatistics:\n")
print(df.describe())

# ➕ Create Total Marks column
df["Total"] = df["Maths"] + df["Physics"] + df["Chemistry"]

# ➗ Create Average Marks column
df["Average"] = df["Total"] / 3

# 🏆 Find top performer
top_student = df.sort_values(by="Total", ascending=False)
print("\nTop Performer:\n", top_student.head(1))

# 📊 Bar Chart: Total Marks
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Total"])

plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# 📈 Scatter Plot: Study Hours vs Marks
plt.figure(figsize=(6,5))
plt.scatter(df["Hours_Studied"], df["Total"])

plt.title("Study Hours vs Total Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Total Marks")

plt.grid()
plt.tight_layout()
plt.show()

# 🔍 High performers (Average > 80)
high_perf = df[df["Average"] > 80]
print("\nHigh Performers:\n", high_perf)