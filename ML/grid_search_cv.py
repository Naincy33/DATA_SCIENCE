from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

# -------------------------
# DATA
# -------------------------
X, y = load_iris(return_X_y=True)

# -------------------------
# MODEL
# -------------------------
model = KNeighborsClassifier()

# -------------------------
# PARAMETERS TO TEST
# -------------------------
params = {
    "n_neighbors": [1,3,5,7],
    "weights": ["uniform", "distance"]
}

# -------------------------
# GRID SEARCH CV
# -------------------------
grid = GridSearchCV(
    model,
    params,
    cv=5
)

# Train
grid.fit(X, y)

# -------------------------
# RESULTS
# -------------------------
print("Best Parameters:", grid.best_params_)

print("Best Score:", grid.best_score_)