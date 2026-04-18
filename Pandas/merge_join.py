
import pandas as pd

employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DeptID": [10, 20, 30]
})

departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "DeptName": ["HR", "Engineering", "Marketing"]
})

inner = pd.merge(employees, departments, on="DeptID")
left = pd.merge(employees, departments, on="DeptID", how="left")
right = pd.merge(employees, departments, on="DeptID", how="right")
outer = pd.merge(employees, departments, on="DeptID", how="outer")

print("INNER JOIN:\n", inner)
print("\nLEFT JOIN:\n", left)
print("\nRIGHT JOIN:\n", right)
print("\nOUTER JOIN:\n", outer)