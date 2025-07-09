from flask import Flask, request, jsonify
from flask_cors import CORS
from prediction_helper import predict

app = Flask(__name__)
CORS(app)  # ✅ Allow access from JS/frontend

@app.route('/')
def home():
    return "Welcome to the Healthcare Premium Prediction API. Use POST /predict to get predictions."

@app.route('/predict', methods=['POST'])
def predict_premium():
    try:
        input_data = request.get_json()
        prediction = predict(input_data)
        return jsonify({'predicted_premium': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
