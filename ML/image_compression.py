import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# -----------------------------
# 1️⃣ LOAD IMAGE
# -----------------------------
img = Image.open("svd2.png")

# Show original image
plt.figure(figsize=(5,5))
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")
plt.show()

# -----------------------------
# 2️⃣ CONVERT TO GRAYSCALE
# -----------------------------
gray = img.convert("L")

# Convert image to matrix
A = np.array(gray)

print("Image Matrix Shape:", A.shape)

# -----------------------------
# 3️⃣ APPLY SVD
# -----------------------------
U, S, Vt = np.linalg.svd(A, full_matrices=False)

print("U shape:", U.shape)
print("S shape:", S.shape)
print("Vt shape:", Vt.shape)

# -----------------------------
# 4️⃣ USER INPUT FOR COMPRESSION
# -----------------------------
k = int(input("Enter value of k: "))

# -----------------------------
# 5️⃣ COMPRESS IMAGE
# -----------------------------
A_compressed = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]

# -----------------------------
# 6️⃣ DISPLAY RESULTS
# -----------------------------
plt.figure(figsize=(12,5))

# Original
plt.subplot(1,2,1)
plt.imshow(A, cmap='gray')
plt.title("Original Image")
plt.axis("off")

# Compressed
plt.subplot(1,2,2)
plt.imshow(A_compressed, cmap='gray')
plt.title(f"Compressed Image (k={k})")
plt.axis("off")

plt.tight_layout()
plt.show()