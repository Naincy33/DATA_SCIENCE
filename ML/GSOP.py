import numpy as np

# -----------------------------
# Step 1: Define vectors
# -----------------------------
v1 = np.array([1, 2, 3], dtype=float)
v2 = np.array([2, 3, 4], dtype=float)
v3 = np.array([3, 4, 6], dtype=float)

vectors = [v1, v2, v3]

# Lists
orthobasis = []
orthonormalbasis = []

# -----------------------------
# Step 2: Gram-Schmidt Process
# -----------------------------
for v in vectors:

    # Remove projections
    w = v - sum(
        (np.dot(v, b) / np.dot(b, b)) * b
        for b in orthobasis
    )

    # Store orthogonal vector
    orthobasis.append(w)

    # Normalize vector
    norm = np.linalg.norm(w)

    if norm > 1e-10:
        orthonormalbasis.append(w / norm)

# -----------------------------
# Step 3: Print Results
# -----------------------------
print("Orthogonal Basis:\n")

for i, b in enumerate(orthobasis):
    print(f"e{i+1} = {b}")

print("\nOrthonormal Basis:\n")

for i, b in enumerate(orthonormalbasis):
    print(f"e{i+1} = {b}")