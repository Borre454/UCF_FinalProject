
from flask import Flask, flash, jsonify, render_template, request
import webbrowser
from flask_cors import CORS, cross_origin
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
from keras.preprocessing.sequence import pad_sequences
from cypher import encode
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

app = Flask(__name__)
CORS(app)

# load the model, and pass in the custom metric function
with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
       model = load_model('first_model_50.h5')

model.summary()

@app.route('/')
def hello():
    # return "this webpage is working"
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def my_form_post():
    body = request.form['body']
    title= request.form['title']

    return f'Title:{title} and Body: {body}'

@app.route("/getvalue/<title>/<body>")
def data(title, body):
    body = body.replace("%20", " ")
    title = title.replace("%20", " ")
    tq = [{'Title':title,'Body':body}]
    df = pd.DataFrame(tq)

    df['indexed'] = df.apply(lambda x: encode(x['Title'], x['Body']), axis=1)
    final = pad_sequences(df['indexed'], value=0, padding='post', maxlen=50)
    # model._make_predict_function()
    f = model.predict_classes(final)

    """Display all data from the collection."""
    return f'B : {f}'
    # return f'prediction --- {f}'

# @app.route('/handle_data' ,methods = ['POST', 'GET'])    
# def handle_data():
#     # if request.method == 'POST':
#     #     title = request.form.get('title')
#     #     body = request.form.get('body')
#     #     return title
#     # else:
#     #     return "hello"
#     # return title
#     title = request.form.get('title')
#     body = request.form.get('body')
#     return title
       
    #    from cypher import encode 
#     # encode(title,body)
        
        
        
        # result = request.form
        # return render_template("result.html",result = result)
    #  return render_template('index.html')

# First try, keeps giving an error that I call variable before defined
# @app.route('/handle_data' ,methods = ['POST', 'GET'])    
# def handle_data():
#     if request.method == 'POST':
#         body = request.form['body']
#         # title = request.form['title']
#         return body
        
    
#     # return "this works"
#     # return title
#     # from cypher import encode 
#     # encode(title,body)
    
if __name__ == '__main__':
    app.run(debug=True)
