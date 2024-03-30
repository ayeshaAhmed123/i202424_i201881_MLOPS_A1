from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from joblib import load

app = Flask(__name__)

# Load the trained model
lr_model = load('linear_regression_model.joblib')

# Define features used in the model
features = ['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json
    
    # Check if all required features are present
    if not all(feature in data for feature in features):
        return jsonify({'error': 'Missing required features'}), 400
    
    # Check if all features are numeric
    for feature in features:
        if not isinstance(data[feature], (int, float)):
            return jsonify({'error': f'Non-numeric value for feature {feature}'}), 400
    
    df = pd.DataFrame(data, index=[0])

    # Scale features
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])

    # Make prediction
    prediction = lr_model.predict(df[features])

    return jsonify({'prediction': float(prediction[0])})

if __name__ == '__main__':
    print("hi From server")
    app.run(host='0.0.0.0', port=5000)

