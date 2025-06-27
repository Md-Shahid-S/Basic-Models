import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
with open('linear_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the scaler
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data.get('data')

        if not features:
            return jsonify({'error': 'No data field found in JSON'}), 400

        print("Received data for prediction:", features)

        input_array = np.array(list(features.values())).reshape(1, -1)

        print("Reshaped input:", input_array)

        # Apply feature scaling
        new_data = scaler.transform(input_array)

        # Predict using the model
        prediction = model.predict(new_data)

        print('Prediction output:', prediction[0])

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
# This code is a Flask application that serves a machine learning model for predictions.
# It loads a pre-trained linear regression model and a scaler from pickle files.