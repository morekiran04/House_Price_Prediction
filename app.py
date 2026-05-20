from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    living_area = int(request.form['living_area'])
    floors = int(request.form['floors'])

    data = pd.DataFrame([[
        bedrooms,
        bathrooms,
        living_area,
        floors
    ]], columns=[
        'number of bedrooms',
        'number of bathrooms',
        'living area',
        'number of floors'
    ])

    prediction = model.predict(data)[0]

    return render_template(
        'index.html',
        prediction=round(prediction, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)