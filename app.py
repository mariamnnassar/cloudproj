from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("model/isolation_forest.joblib")

# List of features expected by the model (in correct order)
model_features = ['V17', 'V14', 'V10', 'V16', 'V12', 'V11', 'V4', 'V3', 'V7', 'V18', 'Time_Hours']

# Mapping from frontend input names to model feature names
input_to_model_map = {
    'Amount': 'V17',
    'Transaction Time': 'Time_Hours',
    'Location Score': 'V14',
    'Merchant Type': 'V10',
    'Card Usage': 'V16',
    'Risk Factor': 'V12',
    'Account Age': 'V11',
    'Spending Pattern': 'V4',
    'Alert Count': 'V3',
    'V7': 'V7',  # لو حابة تغيري الاسم، غيريه كمان بالفرونت
    'V18': 'V18'
}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Convert input data to the format expected by the model
        model_input = {}
        for user_key, model_key in input_to_model_map.items():
            value = data.get(user_key)
            if value is None:
                return jsonify({"error": f"Missing value for {user_key}"}), 400
            model_input[model_key] = float(value)

        # Arrange features in the order required by the model
        input_values = [model_input[feature] for feature in model_features]
        input_array = np.array(input_values).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)[0]
        label = "Fraud" if prediction == -1 else "Legit"

        return jsonify({"prediction": label})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
