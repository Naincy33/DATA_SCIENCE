import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC

# Data
X = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 7],
    [7, 8],
    [8, 8]
])

y = np.array([0, 0, 0, 1, 1, 1])

# Create SVM model
model = SVC(kernel="linear", C=1)

# Train
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

print("Predictions:", y_pred)

# Plot data
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    s=100
)

# Plot support vectors
plt.scatter(
    model.support_vectors_[:, 0],
    model.support_vectors_[:, 1],
    s=200,
    facecolors="none",
    edgecolors="red",
    linewidths=2,
    label="Support Vectors"
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.title("Linear SVM")

plt.legend()

plt.show()