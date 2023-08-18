import os
import sys 
sys.path.append("D:\Breast_Cancer_assignment")
import pandas as pd 
import numpy as np 
import pymongo
from src.logger import logging
from src.exception import CustomException
from src.constant import *
from src.utils.main_utils import Mainutils
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    artifact_folder: str = os.path.join(artifact_folder) # Provide the correct folder path

class DataIngestion:
    def __init__(self):
        self.data_ingestion = DataIngestionConfig()
        self.utils = Mainutils()

    def Pymongo_Config(self, MongoDb_Name, MongoDB_Collection):
        logging.info("Entered into the Pymongo Config of Data Ingestion")
        try:
            client = pymongo.MongoClient(MONGODB_URL)
            db = client[MongoDb_Name]
            collection = db[MongoDB_Collection]
            return collection
        except Exception as e:
            raise CustomException(e, sys) from e

    def data_dataframe(self):
        logging.info('Entered the data_dataframe of Data Ingestion')
        try:
            collection = self.Pymongo_Config(MongoDb_Name=MONGO_DATABASE_NAME, MongoDB_Collection=MONGO_DATABASE_COLLECTION)
            data = collection.find({})
            df = pd.DataFrame(list(data))
            columns_to_drop = ['_id']
            df.drop(columns=columns_to_drop, axis=1, inplace=True)  # Use inplace=True instead of assignment
            logging.info('Exited from the data_dataframe of Data Ingestion')
            return df
        except Exception as e:
            raise CustomException(e, sys) from e

    def file_save(self) -> str:
        logging.info('Entered the file_save of Data Ingestion')
        try:
            df=self.data_dataframe()
            artifact_folder = self.data_ingestion.artifact_folder
            os.makedirs(artifact_folder, exist_ok=True)
            logging.info("Data is received Successfully from MongoDB")
            raw_file_path = os.path.join(artifact_folder, 'Breast_cancer_data.csv')
            df.to_csv(raw_file_path, index=False)
            return raw_file_path
        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_data_ingestion(self):
        try:
            # df = self.data_dataframe()
            file_path = self.file_save()
            logging.info(f'Entered into the Final Step of Data Ingestion and file is saved into {file_path}')
            return file_path
        except Exception as e:
            raise CustomException(e, sys) from e
