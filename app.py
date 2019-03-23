from flask import Flask, request, render_template
import numpy as np
from AdvancedRegression_v3 import apply_algorithm 

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/data")
def data():

    return render_template("data.html")

@app.route("/form", methods=['GET', 'POST'])
def interpret(guess=None, livable_area=None, num_cars=None, garage_area=None, basement_sqft=None, first_fl_sqft=None):
    if request.method == 'POST':
        quality = request.form['OverallQual']
        livable_area = 0
        livable_area = request.form['GrLivArea']
        num_cars = 0
        num_cars = request.form['GarageCars']
        garage_area = 0
        garage_area = request.form['GarageArea']
        basement_sqft = 0
        basement_sqft = request.form['TotalBsmtSF']
        first_fl_sqft = 0
        first_fl_sqft = request.form['1stFlrSF']

        guess = apply_algorithm(quality, livable_area, num_cars, garage_area, basement_sqft, first_fl_sqft)

    return render_template("form.html", guess=guess, livable_area=livable_area, num_cars=num_cars, garage_area=garage_area, basement_sqft=basement_sqft, first_fl_sqft=first_fl_sqft)

if __name__ == '__main__':
    app.run(debug=True)