from sklearn.tree import DecisionTreeClassifier

# Features: [study_hours]
X = [[1], [2], [3], [4], [5]]

# Labels: pass/fail
y = ["fail", "fail", "pass", "pass", "pass"]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[2]]))  # fail
print(model.predict([[5]]))  # pass