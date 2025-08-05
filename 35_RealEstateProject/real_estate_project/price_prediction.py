import joblib
import json
import numpy as np

_model = joblib.load('real_estate.pkl')
_scaling = joblib.load('feature_scaling.pkl')

my_json_file = open("training_data_columns.json" , "r")
my_json_file = json.load(my_json_file)
_features = my_json_file['data_columns']
#print(_features)

area_type = "Super built-up Area"
availability = "Ready To Move"
location = "5th phase jp nagar"
size = 2
total_sqft = 1200
bath = 2
balcony = 2

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

print(np.exp(_model.predict(_scaling.transform([input])))[0])