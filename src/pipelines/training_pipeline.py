import os 
import sys 
import numpy as np 
import pandas as pd 
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Model_Trainer
from src.utils.main_utils import Mainutils
from src.logger import logging
from src.exception import CustomException
from src.constant import * 
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from dataclasses import dataclass


@dataclass
class TrainingConfig:
    para_grid={
    'C':np.linspace(0.001, 1, 20), 'fit_intercept':[True, False]
}
    artifact_folder=os.path.join(artifact_folder,MODEL_FILE_NAME)
    
class Training:
    def __init__(self):
        self.trainingconfig=TrainingConfig()
        self.transformation=DataTransformation()
        self.utils=Mainutils()
        self.model_train=Model_Trainer()
        self.ingestion=DataIngestion()
    def Hyper(self,model):
        try:
            logging.info("Enterd into the hypertuning of model ")
            paragrid=self.trainingconfig.para_grid
            clf=GridSearchCV(model,param_grid=paragrid,cv=10,verbose=3)
            logging.info("model is save into artifacts")
            return clf
        except Exception as e:
            raise CustomException(e,sys) from e
    def Model_evalution(self,model,X_train,y_train,x_test,y_test):
        try:
            clf=self.Hyper(model=model)
            logging.info("Enter into the fitting of the model ")
            clf.fit(X_train,y_train)
            self.utils.save_object(self.trainingconfig.artifact_folder,obj=clf)
            y_pred=clf.predict(x_test)
            score=accuracy_score(y_test,y_pred)
            logging.info(f"After the Hypertuning of the model accuracy is {score}")
            return score
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def run_pipeline(self)->None:
        try:
            model=self.model_train.initiate_model_train()
            file_path=self.ingestion.initiate_data_ingestion()
            X_train_scaled,X_test_scaled,y_train,y_test=self.transformation.initiate_data_Transfomration(file_path=file_path)
            score=self.Model_evalution(model,X_train=X_train_scaled,y_train=y_train,x_test=X_test_scaled,y_test=y_test)
            logging.info(f"Congratulation Model is train and their accuracy is {score}")
        except Exception as e:
            raise CustomException(e,sys) from e


            
            

    
     
        
        
        
        