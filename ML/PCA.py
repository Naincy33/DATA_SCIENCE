import numpy as np

# -----------------------------
# Step 1: Given Data
# -----------------------------
X = np.array([
    [4, 8, 13, 7],
    [11, 4, 5, 14]
])

print("Original Data:\n", X)

# -----------------------------
# Step 2: Compute Mean
# -----------------------------
mean = np.mean(X, axis=1, keepdims=True)

print("\nMean:\n", mean)

# -----------------------------
# Step 3: Center the Data
# -----------------------------
X_centered = X - mean

print("\nCentered Data:\n", X_centered)

# -----------------------------
# Step 4: Covariance Matrix
# -----------------------------
N = X.shape[1]

cov_matrix = (1 / (N - 1)) * (X_centered @ X_centered.T)

print("\nCovariance Matrix:\n", cov_matrix)

# -----------------------------
# Step 5: Eigenvalues & Eigenvectors
# -----------------------------
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("\nEigenvalues:\n", eigenvalues)

print("\nEigenvectors:\n", eigenvectors)

# -----------------------------
# Step 6: Select Principal Component
# -----------------------------
idx = np.argmax(eigenvalues)

principal_vector = eigenvectors[:, idx]

print("\nPrincipal Eigenvector:\n", principal_vector)

# -----------------------------
# Step 7: Normalize Eigenvector
# -----------------------------
e1 = principal_vector / np.linalg.norm(principal_vector)

print("\nNormalized Eigenvector:\n", e1)

# -----------------------------
# Step 8: Project Data to 1D
# -----------------------------
X_reduced = e1.T @ X_centered

print("\n1D Reduced Data:\n", X_reduced)