from flask import Flask, render_template, request, redirect, url_for
from joblib import load
import numpy as np
import transformers as t

# load the pipeline object1
model = load("predictive-analytics\ciclist-accident-classification.joblib")


def requestResults(data):
    # [latitud, longitud, dia_semana, delegacion_inicio, hora_creacion]
    prediction = model.predict(np.array(data).reshape(1, -1))
    return prediction

def preprocess_data(latitude, longitude, day, town, time):
    latitude, longitude = t.transform_geo(latitude, longitude)
    town = t.transform_town(town) 
    day = t.transform_day(day)
    time = t.transform_time(time)
    return [latitude, longitude, day, town, time]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        town = request.form['town']
        day = request.form['day']
        time = request.form['time']
        
        data_transformed = preprocess_data(latitude, longitude, day, town, time)
        response = requestResults(data_transformed)
        if response == 0:
            return """<head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>¿Viviré?</title>
                            <!-- CSS only -->
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                        </head>
                       <h2 style='color: blue;'> ¡Adelante pedaleante! </h2>
                       <h3 style='color: blue;'> Es muy poco probable que sufras un accidente :) </h3>"""
        else:
            return """<head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>¿Viviré?</title>
                            <!-- CSS only -->
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                        </head>
                    <h2 style='color: red;'> ¡Acercandose, el peligro viene ya! </h2>
                    <h2 style='color: red;'> ¡Ojo! Es muy probable que te suceda un accidente en esta zona :O </h2>
                    """

if __name__ == '__main__':
    app.run(debug=True)
