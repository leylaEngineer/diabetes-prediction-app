from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    # Debug: print incoming data
    print("Incoming data:", data)
    
    # Convert inputs to float
    for key in data:
        data[key] = float(data[key])  # Convert all inputs to float

    # Create input DataFrame
    input_df = pd.DataFrame([data])
    print("Input DataFrame columns:", input_df.columns.tolist())  # Debugging line
    
    # Ensure the DataFrame has the correct features
    required_features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    # Check for missing features
    missing_features = [feature for feature in required_features if feature not in input_df.columns]
    if missing_features:
        print("Missing features:", missing_features)
        return jsonify({'error': f'Missing features: {missing_features}'}), 400

    input_df = input_df[required_features]  # Filter to keep only required features

    # Make prediction
    prediction = model.predict(input_df)
    return jsonify({'prediction': 'Yes' if prediction[0] == 1 else 'No'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)