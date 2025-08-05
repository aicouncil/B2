import joblib
import json
import numpy as np
from flask import Flask,request

app = Flask(__name__)

_model = joblib.load('real_estate.pkl')
_scaling = joblib.load('feature_scaling.pkl')

my_json_file = open("training_data_columns.json" , "r")
my_json_file = json.load(my_json_file)
_features = my_json_file['data_columns']
#my_json_file.close()

@app.route('/predict', methods=['POST'])
def predict_home_price():

    if request.is_json:
        data = request.json
    else:
        data = request.form

    #Extract data from request
    area_type = data.get('areaType')
    availability = data.get('availability')
    location = data.get('location')
    size = data.get('size')
    total_sqft = data.get('totalSqft')
    bath = data.get('bath')
    balcony = data.get('balcony')

    area_type = area_type
    availability = availability
    location = location
    size = size
    total_sqft = total_sqft
    bath = bath
    balcony = balcony

    area_type_function = lambda area_type : 0 if area_type.lower().strip() == 'super built-up area' else 1
    availability_function = lambda availability : 0 if availability == 'Ready To Move' else 1

    input = np.zeros(len(_features))

    input[0] = area_type_function(area_type)
    input[1] = availability_function(availability)
    input[2] = size
    input[3] = total_sqft
    input[4] = bath
    input[5] = balcony

    input[_features.index("location_" + location)] = 1

    price_predicted = np.exp(_model.predict(_scaling.transform([input])))[0]
    return {"Predicted_Price" : price_predicted}



app.run(debug=True)