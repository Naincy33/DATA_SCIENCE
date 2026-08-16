from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features
X = [
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 80],
    [6, 85],
    [7, 90]
]

# Labels
y = [
    "Fail",
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Model
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 7))

plot_tree(
    model,
    feature_names=["Study Hours", "Attendance"],
    class_names=["Fail", "Pass"],
    filled=True
)

plt.show()