from AdvancedRegression_v3 import apply_algorithm 
import os
import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    url_for,
    redirect)

app = Flask(__name__)



@app.route("/")
def index():

    return render_template("index.html")

# Create a list to hold our data
my_data = []


@app.route("/data")
def data():

    return render_template("data.html")

@app.route("/form", methods=['GET', 'POST'])
def interpret(guess=None, quality=None, livable_area=None, num_cars=None, garage_area=None, basement_sqft=None, first_fl_sqft=None): 
    if request.method == 'POST':
        quality = request.form['OverallQual']
        livable_area = request.form['GrLivArea']
        num_cars = request.form['GarageCars']
        garage_area = request.form['GarageArea']
        basement_sqft = request.form['TotalBsmtSF']
        first_fl_sqft = request.form['1stFlrSF']
        print(quality)


        form_data = {
            "quality": quality,
            "livable area": livable_area,
            "number of cars": int(num_cars),
            "garage area": garage_area,
            "basement sqft": basement_sqft,
            "first fl sqft": first_fl_sqft,

        }

        my_data.append(form_data)



        guess = apply_algorithm(quality, livable_area, num_cars, garage_area, basement_sqft, first_fl_sqft)


    return render_template("form.html", guess=guess, quality=quality, livable_area=livable_area, num_cars=num_cars, garage_area=garage_area, basement_sqft=basement_sqft, first_fl_sqft=first_fl_sqft)
    #return render_template("form.html")



@app.route("/dashboard")
def dashboard():

    return render_template("/dashboard.html")

@app.route("/jsonified")
def jsonified():
   
    print(my_data)
    return jsonify(my_data)



if __name__ == "__main__":
    app.run()
