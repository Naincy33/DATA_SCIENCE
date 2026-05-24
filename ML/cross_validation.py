from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Data
X, y = load_iris(return_X_y=True)

# Model
model = RandomForestClassifier()

# Cross Validation
scores = cross_val_score(model, X, y, cv=5)

print("Scores:", scores)

print("Average Accuracy:", scores.mean())