import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

def Value_predictor(predict_list):
    to_predict = np.array(predict_list).reshape(1,12)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        predict_list = request.form.to_dict()
        predict_list = list(predict_list.values())
        predict_list = list(map(int, predict_list))
        result = Value_predictor(predict_list)
        if int(result)==1:
            prediction = 'Income more than 50K'
        else:
            prediction = 'Income less than 50K'
        return render_template('result.html', prediction=prediction)