from crypt import methods
import pickle
from flask import Flask,request,app,jsonify,render_template,url_for
import pandas as pd
import numpy as np

# instalize  the app
app = Flask(__name__)

# Load the Model
regmodel = pickle.load('regmodel.pkl','rb')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data = request.json('data')
    print(data)
    
