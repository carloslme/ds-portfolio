from flask import Flask, render_template, request, redirect, url_for
from joblib import load
import numpy as np
import transformers as t

# load the pipeline object1
model = load("D:\Cursos\ds-portfolio\ds-portfolio\predictive-analytics\ciclist-accident-classification.joblib")


def requestResults(data):
    # [latitud, longitud, dia_semana, clas_con_f_alarma, tipo_entrada, hora_creacion]
    # [latitud, longitud, dia_semana, delegacion_inicio, hora_creacion]
    values = np.array([19.47, -99.12, 1.0, 19.0])
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
        return '{}'.format(str(response))

if __name__ == '__main__':
    app.run(debug=True)
