import pandas as pd

# Sample DataFrame
data = {
    "name": ["Ram", "Shyam", "Aman", "Riya"],
    "age": [25, 30, 22, 28],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune"],
    "first name": ["R", "S", "A", "R"],   # space wala column
    "class": ["Physics", "Math", "Physics", "Chemistry"]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# 1️⃣ Basic filtering
print("\nAge > 25:")
print(df.query("age > 25"))

# 2️⃣ Multiple conditions
print("\nAge > 25 and city == Delhi:")
print(df.query("age > 25 and city == 'Delhi'"))

# 3️⃣ String filtering
print("\nName == Ram:")
print(df.query("name == 'Ram'"))

# 4️⃣ Column with space (backticks)
print("\nFirst name == R:")
print(df.query("`first name` == 'R'"))

# 5️⃣ Using Python variable
age_limit = 26
print("\nUsing variable age_limit:")
print(df.query("age > @age_limit"))

# 6️⃣ Chained comparison
print("\nAge between 23 and 30:")
print(df.query("23 < age < 30"))

# 7️⃣ Reserved keyword column
print("\nClass == Physics:")
print(df.query("`class` == 'Physics'"))

# 8️⃣ Case sensitive check
print("\nCity == delhi (wrong case):")
print(df.query("city == 'delhi'"))   # empty output

print("\nCity == Delhi (correct case):")
print(df.query("city == 'Delhi'"))