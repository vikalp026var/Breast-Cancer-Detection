from flask import Flask,render_template,request,app,jsonify
from src.exception import CustomException
from src.logger import logging
import os ,sys
from src.pipelines.training_pipeline import Training
from src.pipelines.prediction_pipeline import Prediction


app=Flask(__name__)
@app.route("/")
def index():
    return 'Welcome to Breast Cancer Detection App'
@app.route("/train")
def train():
    try:
        obj=Training()
        obj.run_pipeline()
        return render_template('index.html')
    except Exception as e:
        raise CustomException(e,sys)
    
@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        if request.method=='POST':
            obj=Prediction()
            results=obj.run_pipeline()
            return render_template('index.html',result=results)
    except Exception as e:
        raise CustomException(e,sys) from e

if __name__ == '__main__':
    app.run(debug=True,port=8080)