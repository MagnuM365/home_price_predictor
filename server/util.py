import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, land_area, floor, bhk, bathroom):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1  # location not found

    x = np.zeros(len(__data_columns))
    x[0] = land_area
    x[1] = floor
    x[2] = bhk
    x[3] = bathroom
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0]/100, 2)

def get_location_names():
    return __locations
    
def load_saved_artifacts():
    print("Loading artifacts...")
    global __data_columns
    global __locations
    global __model
    
    with open("./artifacts/house_price_predictor_columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]
        
    with open("./artifacts/house_price_predictor_model.pkl", 'rb') as f:
        __model = pickle.load(f)

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())