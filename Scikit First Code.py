import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


data = np.array([
    [1, 50, 0],
    [2, 60, 0],
    [3, 65, 0],
    [4, 70, 0],
    [5, 75, 1],
    [6, 80, 1],
    [7, 85, 1],
    [8, 90, 1],
    [9, 95, 1],
    [10,100, 1],
    ])

X = data[:, :2]
y = data[:, 2]

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state= 12)
model = RandomForestClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print ("Accuracy", accuracy)
print("\nClassification Report:\n", report)

new_data = np.array([[7, 80], [3, 50]])  # Example: [Hours_Studied, Attendance]
predictions = model.predict(new_data)
print("\nPredictions for new data:", predictions)