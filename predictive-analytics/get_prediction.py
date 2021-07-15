from flask import Flask, render_template, request, redirect, url_for
from joblib import load
import numpy as np

# load the pipeline object
model = load("D:\Cursos\ds-portfolio\ds-portfolio\predictive-analytics\ciclist-accident-classification.joblib")


def requestResults():
    values = np.array([19.47, -99.12, 1.0, 1.0, 3.0, 20.0])
    prediction = model.predict(values.reshape(1, -1))
    return prediction


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        pass
    return 'Hola prrosss'

if __name__ == '__main__':
    app.run(debug=True)
