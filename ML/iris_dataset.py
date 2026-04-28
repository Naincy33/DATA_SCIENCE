import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('data.csv')  # Replace with your actual CSV file path
X = data.iloc[:, :-1]  # All columns except the last as features
y = data.iloc[:, -1]   # Last column as label
model = RandomForestClassifier()
model.fit(X, y)
predictions = model.predict(X)  # Predict on the same/new data (for demonstration)
print(predictions)  # Display predictions₹