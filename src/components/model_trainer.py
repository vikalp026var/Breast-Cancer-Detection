import os 
import sys 
import pandas as pd 
import numpy as np 
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.constant import * 
from src.utils.main_utils import Mainutils
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import accuracy_score
from dataclasses import dataclass

@dataclass
class ModelTrainConfig:
    model = {
        'LogisticRegression': LogisticRegression(),
        'GaussianNB': GaussianNB(),
        'DecisionTreeClassifier': DecisionTreeClassifier()
    }

class Model_Trainer:
    def __init__(self):
        self.model_train_config = ModelTrainConfig()
        self.data_transformation_config = DataTransformation()
        self.data_ingestion_config = DataIngestion()
        self.utils=Mainutils()
    
    def models(self, models, X_train, y_train, X_test, y_test):
        logging.info("Enter the definition of models")
        try:
            result = {}
            for model_name, model in models.items():
                  model.fit(X_train, y_train)  # Train the model
                  logging.info(f'Model is train with {model}')
                  y_pred = model.predict(X_test)  # Make predictions
                  logging.info(f"Get the prediction on the training model ")
                  accuracy = accuracy_score(y_test, y_pred)
                  logging.info(f"Ande get the accuracy of the model is {model} is {accuracy}")
                  result[model_name] = accuracy
            
            
            best_model_name = max(result, key=result.get)
            logging.info(f'Get the best model is {best_model_name}')
            best_accuracy = result[best_model_name]
            model=models[best_model_name]

            # logging.info(f"Accuracy of {best_model_name} is {best_accuracy:.2f}")
            # logging.info(f"Best model is {best_model_name} and its accuracy is {best_accuracy:.2f}")

            # best_model_name = [name for name, accuracy in models.items() if accuracy == best_accuracy]

            # logging.info(f"Accuracy of {best_model_name[0]} is {best_accuracy:.2f}")
            # logging.info(f"Best model is {best_model_name[0]} and its accuracy is {best_accuracy:.2f}")
            return model
        except Exception as e:
            raise CustomException(e, sys) from e

    
    def initiate_model_train(self):
        logging.info("Entered into initiate model train of Model_Trainer class")
        try:
            models = self.model_train_config.model
            file_path = self.data_ingestion_config.initiate_data_ingestion()
            X_train, X_test, y_train, y_test = self.data_transformation_config.initiate_data_Transfomration(file_path=file_path)
            model = self.models(models=models, X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
            return model
        except Exception as e:
            raise CustomException(e, sys) from e
