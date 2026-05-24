from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

# Data
X, y = load_iris(return_X_y=True)

# Model
model = KNeighborsClassifier()

# Hyperparameters to test
params = {
    "n_neighbors": [1,3,5,7,9]
}

# Grid Search
grid = GridSearchCV(model, params, cv=5)

grid.fit(X, y)

# Best result
print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)