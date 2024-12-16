from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
from sklearn.preprocessing import StandardScaler


data = {
    "size":[ 1400, 1600, 1700, 1875, 1100, 1550, 2350 ],
    "num_rooms": [3, 4, 4, 5, 2, 3, 5],
    "location": ["lagos", "rivers", "ondo", "lagos", "rivers", "lagos", "ondo"],
    "price": [300000, 450000, 550000, 620000, 200000, 480000, 750000]
}
    
df = pd.DataFrame(data)

features = df[['size', 'num_rooms', 'location']]
target = df['price']

features = pd.get_dummies(features, columns= ['location'])
scalar = StandardScaler()
features_scaled = scalar.fit_transform(features)

target_binary = (target > 500000).astype(int)

X_train, X_test, y_train, y_test= train_test_split(features_scaled, target_binary, test_size= 0.2, random_state= 12)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Sigmoid for binary classification
])

model.compile(optimizer = 'adam',
              loss ='binary_crossentropy',
              metrics = ['accuracy'])

model.fit(X_train, y_train, epochs = 10, batch_size = 4,
          validation_split=0.2)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy {accuracy * 100:.2f}%")

predictions = model.predict(X_test)
predictions_binary = (predictions > 0.5).astype(int)


results = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': predictions_binary.flatten()
})
print(results)