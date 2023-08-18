import os 
import sys 
import pandas as pd 
import numpy as np 
from src.utils.main_utils import Mainutils
from src.logger import logging
from src.exception import CustomException
from src.constant import *
from flask import request,app
from dataclasses import dataclass

@dataclass
class PredictionConfig:
    prediction=os.path.join(PREDICTION_FILE)
    artifact_folders=os.path.join(artifact_folder,MODEL_FILE_NAME)
    preprocessor=os.path.join(artifact_folder,'preprocessor.pkl')

class Prediction:
    def __init__(self):
        self.predictionconfig=PredictionConfig()
        self.utils=Mainutils()


    def load_object(self):
        try:
            logging.info("Enter the load_object of Prediction file ")
            model=self.utils.load_object(self.predictionconfig.artifact_folders)
            preprocessor=self.utils.load_object(self.predictionconfig.preprocessor)
            logging.info("Successfully load the model & preprocessor pickle file ")
            return model,preprocessor
        except Exception as e:
            logging.info(f"!!!!Expection is {e}")
            raise CustomException(e,sys) from e
    def get_prediction(self):
        try:
            logging.info("Enter in get_prediction of Main_utils")
            model,preprocessor=self.load_object()
            radius_mean=float(request.form.get("radius_mean"))
            texture_mean=float(request.form.get("texture_mean"))
            perimeter_mean=float(request.form.get("perimeter_mean"))
            area_mean=float(request.form.get("area_mean"))
            smoothness_mean=float(request.form.get("smoothness_mean"))
            compactness_mean=float(request.form.get("compactness_mean"))
            concavity_mean=float(request.form.get("concavity_mean"))
            concave_points_mean=float(request.form.get("concave_points_mean"))
            symmetry_mean=float(request.form.get("symmetry_mean"))
            fractal_dimension_mean=float(request.form.get("fractal_dimension_mean"))
            radius_se=float(request.form.get("radius_se"))
            texture_se=float(request.form.get("texture_se"))
            perimeter_se=float(request.form.get("perimeter_se"))
            area_se=float(request.form.get("area_se"))
            smoothness_se=float(request.form.get("smoothness_se"))
            compactness_se=float(request.form.get("compactness_se"))
            concavity_se=float(request.form.get("concavity_se"))
            concave_points_se=float(request.form.get("concave_points_se"))
            symmetry_se=float(request.form.get("symmetry_se"))
            fractal_dimension_se=float(request.form.get("fractal_dimension_se"))
            radius_worst=float(request.form.get("radius_worst"))
            texture_worst=float(request.form.get("texture_worst"))
            perimeter_worst=float(request.form.get("perimeter_worst"))
            area_worst=float(request.form.get("area_worst"))
            smoothness_worst=float(request.form.get("smoothness_worst"))
            compactness_worst=float(request.form.get("compactness_worst"))
            concavity_worst=float(request.form.get("concavity_worst"))
            concave_points_worst=float(request.form.get("concave_points_worst"))
            symmetry_worst=float(request.form.get("symmetry_worst"))
            fractal_dimension_worst=float(request.form.get("fractal_dimension_worst"))
            
            new_data=preprocessor.fit_transform([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
            predict=model.predict(new_data)
            logging.info(f'Prediction is {predict}')
            if(predict[0]==1):
                logging.info(f"Prediction is {predict[0]}")
                result=" Diagonsis is !!Yes"
            else:
                result="Diagonsis is !No"
            logging.info(f"Exited from predict file of Prediction and the prediction is {result} ")
            return result
        except Exception as e:
            raise CustomException(e,sys) from e
    def run_pipeline(self):
        try:
            logging.info("Enter the run pipeline of Prediction")
            result=self.get_prediction()
            logging.info("Congrautaions well played Project is on the final step ")
            print(result)
            
        except Exception as e:
            raise CustomException(e,sys) from e
        # 


        
        