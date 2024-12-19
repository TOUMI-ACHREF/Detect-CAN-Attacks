from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

tab = ["Ordinale message", "Attaque DoS", "Attaque de Fuzzing", "Attaque par Usurpation d'Identité"]

# Load your pre-trained model
model = joblib.load('securityModel4.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features', [])
    
    if not features:
        return jsonify({"error": "No features provided"}), 400

    try:
        # Perform prediction using the loaded model
        prediction = model.predict([features])
        print("Prediction : ", prediction)
        # Format the output as needed
        return jsonify({"prediction": tab[prediction[0]]})
    except Exception as e:
        print("Error occurred:", e)  # Print to console
        return jsonify({"error": "Prediction failed"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
