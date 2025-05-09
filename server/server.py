from flask import Flask, jsonify, request
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    land_area = float(request.form['land_area'])
    location = request.form['location']  # Keep as string
    floor = float(request.form.get('floor', 1))
    bhk = float(request.form['bhk'])
    bathroom = float(request.form['bathroom'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, land_area, floor, bhk, bathroom)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

    
if __name__ == "__main__":
    print("Starting server")
    util.load_saved_artifacts()
    app.run()
