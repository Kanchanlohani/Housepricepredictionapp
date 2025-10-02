from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # 👈 allow frontend to talk to backend

# Load model
model_data = joblib.load("house_price_model.pkl")
model = model_data["model"]
columns = model_data["columns"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    print("Received Data:", data)

    # Build DataFrame
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    # Predict
    prediction = model.predict(df)[0]
    return jsonify({"price": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)
