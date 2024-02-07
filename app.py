import pandas as pd
import numpy as np
from flask import Flask, request, jsonify,render_template
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pickle

# Load the saved model and transformer with pickle
with open('E:/DPS Challenge/dps_model_and_transformer.pkl', 'rb') as file:
    saved_objects = pickle.load(file)
    model = saved_objects['model']
    preprocessor = saved_objects['transformer']

# Create the Flask application object
app = Flask(__name__,template_folder='.templates')

@app.route('/')
def home():
    return render_template('home1.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    if request.method == 'POST':
        # Get the input values from the form
        data = request.get_json()
        year = int(data['year'])
        month = int(data['month'])
        if month < 1 or month > 12:
            return jsonify({"error": "Invalid month. Please enter a value between 1 and 12."})
        
        # Prepare the input data for prediction
        #X_pred = [[year, month]]

        # Prepare the input data for prediction as a pandas DataFrame
        input_data = pd.DataFrame({'Year': [year], 'Month': [month]})
        X_pred_preprocessed = preprocessor.transform(input_data )
        # Make the prediction
        prediction = model.predict(X_pred_preprocessed )
        
        # Convert the prediction to a list
        predicted_value = int(round(prediction[0]))
       
        
        # Create the response dictionary
        response = {"prediction": predicted_value}
        
        # Return the response as JSON
        return jsonify(response)
    
    # Render the home template for GET requests
    

    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

