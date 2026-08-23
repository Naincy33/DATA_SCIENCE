import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("project_01/student.csv")

# -----------------------------
# FEATURES & TARGET
# -----------------------------

X = df[["Study_Hours", "Attendance"]]
y = df["Result"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# FEATURE SCALING
# -----------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# SVM MODEL
# -----------------------------

model = SVC(
    kernel="rbf",
    C=1,
    gamma="scale"
)

# -----------------------------
# TRAIN
# -----------------------------

model.fit(X_train_scaled, y_train)

# -----------------------------
# PREDICTION
# -----------------------------

y_pred = model.predict(X_test_scaled)

# -----------------------------
# EVALUATION
# -----------------------------

print("Accuracy:",
      accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nPrecision:",
      precision_score(y_test, y_pred, pos_label="Pass"))

print("Recall:",
      recall_score(y_test, y_pred, pos_label="Pass"))

print("F1 Score:",
      f1_score(y_test, y_pred, pos_label="Pass"))