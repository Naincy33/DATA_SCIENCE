import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# --------------------------------
# 1. LOAD DATA
# --------------------------------

df = pd.read_csv("spam.csv", encoding="latin-1")

print(df.head())
print(df.columns)

# --------------------------------
# 2. KEEP REQUIRED COLUMNS
# --------------------------------

df = df[["v1", "v2"]]

df.columns = ["label", "message"]

# Remove missing values
df = df.dropna()

# --------------------------------
# 3. FEATURES AND TARGET
# --------------------------------

X = df["message"]
y = df["label"]

# --------------------------------
# 4. TRAIN TEST SPLIT
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# --------------------------------
# 5. TEXT → NUMBERS
# --------------------------------

vectorizer = CountVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)

X_test_vec = vectorizer.transform(X_test)

print("Training shape:", X_train_vec.shape)
print("Testing shape :", X_test_vec.shape)

# --------------------------------
# 6. NAIVE BAYES MODEL
# --------------------------------

model = MultinomialNB()

model.fit(X_train_vec, y_train)

# --------------------------------
# 7. PREDICTION
# --------------------------------

y_pred = model.predict(X_test_vec)

# --------------------------------
# 8. EVALUATION
# --------------------------------

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nPrecision:")
print(
    precision_score(
        y_test,
        y_pred,
        pos_label="spam"
    )
)

print("\nRecall:")
print(
    recall_score(
        y_test,
        y_pred,
        pos_label="spam"
    )
)

print("\nF1 Score:")
print(
    f1_score(
        y_test,
        y_pred,
        pos_label="spam"
    )
)

# --------------------------------
# 9. CONFUSION MATRIX
# --------------------------------

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# --------------------------------
# 10. CLASSIFICATION REPORT
# --------------------------------

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)

# --------------------------------
# 11. TEST YOUR OWN MESSAGE
# --------------------------------

new_message = [
    "Congratulations! You have won a free prize"
]

new_message_vec = vectorizer.transform(new_message)

prediction = model.predict(new_message_vec)

print("\nPrediction:", prediction[0])