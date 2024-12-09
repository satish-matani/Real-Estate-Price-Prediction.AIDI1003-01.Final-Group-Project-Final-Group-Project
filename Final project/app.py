import os
from flask import Flask, request, jsonify
import joblib
import numpy as np
 
# Load the trained model and scaler
model = joblib.load('xgboost_model.pkl')
scaler = joblib.load('scaler.pkl')
 
app = Flask(__name__)
 
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json(force=True)
   
    # Convert data into an array
    features = np.array(data['features']).reshape(1, -1)
   
    # Scale features
    features_scaled = scaler.transform(features)
   
    # Make a prediction
    prediction = model.predict(features_scaled)
   
    # Convert prediction to a float
    prediction_float = float(prediction[0])
   
    # Return the prediction as JSON
    return jsonify({'SalePrice': prediction_float})
 
@app.route('/')
def home():
    return """
    <html>
        <head>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background: linear-gradient(135deg, #f2f2f2, #e0e0e0);
                    margin: 0;
                    padding: 0;
                    position: relative;
                }
 
                .container {
                    width: 80%;
                    margin: auto;
                    padding-top: 50px;
                    text-align: center;
                }
 
                h1 {
                    font-size: 36px;
                    color: #333;
                    margin-bottom: 20px;
                    font-weight: bold;
                }
 
                h2, h3 {
                    font-size: 24px;
                    color: #444;
                    margin-bottom: 10px;
                }
 
                h4 {
                    font-size: 20px;
                    color: #666;
                }
 
                .table-container {
                    margin-top: 30px;
                    background-color: #ffffff;
                    border-radius: 10px;
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    display: inline-block;
                    width: 70%;
                    text-align: center;
                }
 
                table {
                    width: 100%;
                    border-collapse: collapse;
                    font-size: 18px;
                }
 
                table, th, td {
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: center;
                }
 
                th {
                    background-color: #006400; /* Bottle Green */
                    color: white;
                    font-size: 20px;
                }
 
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
 
                tr:hover {
                    background-color: #e6f7ff;
                }
 
                footer {
                    margin-top: 50px;
                    padding: 20px;
                    background-color: #333;
                    color: white;
                    font-size: 16px;
                    text-align: center;
                }
 
                .submitted-to {
                    position: absolute;
                    bottom: 20px;
                    right: 20px;
                    font-size: 18px;
                    color: #333;
                    font-weight: bold;
                    background-color: rgba(255, 255, 255, 0.8);
                    padding: 10px;
                    border-radius: 5px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>AIDI 1003 - Machine Learning Frameworks</h1>
                <h2> Real Estate Price Prediction</h2>
                <h3>Group Members:</h3>
               
                <div class="table-container">
                    <table>
                        <tr>
                            <th>Name</th>
                            <th>Student ID</th>
                        </tr>
                        <tr>
                            <td>Satish Kumar</td>
                            <td>200574904</td>
                        </tr>
                        <tr>
                            <td>Dhyan Nitin Trivedi</td>
                            <td>200565531</td>
                        </tr>
                        <tr>
                            <td>Anmol Toor</td>
                            <td>200578497</td>
                        </tr>
                        <tr>
                            <td>Harsh Bhadreshbhai Patel</td>
                            <td>200575814</td>
                        </tr>
                    </table>
                </div>
            </div>
 
            <div class="submitted-to">
                Submitted to: Ethan Davis
            </div>
 
            <footer>
                <p>&copy; 2024 | Final Group Project</p>
            </footer>
        </body>
    </html>
    """
 
if __name__ == '__main__':
    # Add this for deployment on Heroku or production
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
 