from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Load the trained model
model_path = "model/isolation_forest.joblib"
print("Loading model from:", os.path.abspath(model_path))
model = joblib.load(model_path)

# List of features expected by the model (in correct order)
model_features = ['V3', 'V14', 'V17', 'V12', 'V10', 'V7', 'V1', 'V4', 'V16', 'Time_Hours']

# Mapping from frontend input names to model feature names
input_to_model_map = {
    'Alert Count': 'V3',
    'Location Score': 'V14',
    'Amount': 'V17',
    'Risk Factor': 'V12',
    'Merchant Type': 'V10',
    'Card Usage': 'V7',
    'Transaction Category': 'V1',
    'Spending Pattern': 'V4',
    'Account Age': 'V16',
    'Transaction Time': 'Time_Hours'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  
        
        # Convert input data to the format expected by the model
        model_input = {}
        print("Received data:", data)
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
        label = "Fraud" if prediction == 1 else "Not fraud" 
        
        return jsonify({"prediction": label})

    except Exception as e:
        print("Error occurred:", e)   
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)