from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained model and encoders
model = joblib.load('best_accident_forecast_model.pkl')
category_encoder = joblib.load('category_encoder.pkl')
type_encoder = joblib.load('type_encoder.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Parse JSON input
    data = request.get_json()

    # Extract input values
    year = data.get('year')
    month = data.get('month')
    category = data.get('category')
    type_ = data.get('type')

    # Validate inputs
    if None in [year, month, category, type_]:
        return jsonify({"error": "Missing one or more input fields: year, month, category, type"}), 400

    # Encode category and type
    try:
        category_encoded = category_encoder.transform([category])[0]
        type_encoded = type_encoder.transform([type_])[0]
    except ValueError as e:
        return jsonify({"error": f"Invalid category or type: {str(e)}"}), 400

    # Prepare input for prediction
    input_features = pd.DataFrame({
        'JAHR': [year],
        'Month': [month],
        'Category_Encoded': [category_encoded],
        'Type_Encoded': [type_encoded]
    })

    # Make prediction
    try:
        prediction = model.predict(input_features)[0]
    except Exception as e:
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

    # Return the prediction
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
