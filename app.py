# app.py
from flask import Flask
import joblib
import os

app = Flask(__name__)

# Load model
try:
    model = joblib.load("model.pkl")
    print("Model loaded successfully for deployment")
except:
    print("Error loading model")
    model = None

@app.route("/")
def home():
    if model:
        return "ML Model Deployed Successfully!"
    else:
        return "Model not available!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)