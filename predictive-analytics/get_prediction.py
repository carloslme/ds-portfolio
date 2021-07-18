from flask import Flask, render_template, request, redirect, url_for
from joblib import load
import numpy as np

# load the pipeline object
model = load("D:\Cursos\ds-portfolio\ds-portfolio\predictive-analytics\ciclist-accident-classification.joblib")


def requestResults():
    # [latitud, longitud, dia_semana, clas_con_f_alarma, tipo_entrada, hora_creacion]
    # [latitud, longitud, dia_semana, delegacion_inicio, hora_creacion]
    values = np.array([19.47, -99.12, 1.0, 19.0])
    prediction = model.predict(values.reshape(1, -1))
    return prediction

def preprocess_data(latitude, longitude, day, time):
    data = [latitude, longitude ]
    return data

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
        print(latitude)
        print(longitude)
        print(town)
        print(day)
        print(time)
        #requestResults(preprocess_data(latitude, longitude, day, time))
        return 'Hola prrosss'

if __name__ == '__main__':
    app.run(debug=True)
