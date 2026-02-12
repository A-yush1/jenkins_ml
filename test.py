# test.py
import joblib
import os
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

print("Testing model...")

# Check if model exists
if not os.path.exists("model.pkl"):
    print("Error: model.pkl not found!")
    exit(1)

# Load model
model = joblib.load("model.pkl")
print("Model loaded successfully")

# Load test data
X, y = load_iris(return_X_y=True)

# Make predictions
predictions = model.predict(X)

# Calculate accuracy
accuracy = accuracy_score(y, predictions)
print(f"Model test accuracy: {accuracy:.4f}")

if accuracy > 0.8:
    print("Model test PASSED")
else:
    print("Model test FAILED")
    exit(1)