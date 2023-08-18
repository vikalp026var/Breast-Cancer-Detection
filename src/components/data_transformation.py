import os 
import sys 
import pandas  as pd 
import numpy as np 
from src.logger import logging
from src.exception import CustomException
from src.utils.main_utils import Mainutils
from src.constant import * 
from src.components.data_ingestion import DataIngestion
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass 
class DataTranformationConfig:
    preprocesser_file=os.path.join(artifact_folder,preprocessor)
    train_data=os.path.join(artifact_folder,'train.csv')
    test_data=os.path.join(artifact_folder,'test.csv')

class DataTransformation:
    def __init__(self):
        self.datatransformation=DataTranformationConfig()
        self.utils=Mainutils()



    def Data_read(self,file_path):
        logging.info('Entered into the Data read from artifact folder')
        try:
            df=pd.read_csv(file_path)
          #   df['diagnosis']=df['diagnosis'].map({'M':1,'B':0})
            logging.info("Exited from Data_read of Data Tranformation")
            return df 
        except Exception as e:
            raise CustomException(e,sys) from e
        


    def Scaling_data(self,file_path):
        logging.info("Entered into data Scaling function of Data Tranformation")
        try:
            df=self.Data_read(file_path=file_path)
            X=df.drop(columns=['diagnosis'],axis=1)
            y=df['diagnosis']
            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42)
            preprocessor=StandardScaler()
            preprocessor_path=self.datatransformation.preprocesser_file
          #   os.makedirs(preprocessor_path,exist_ok=True)
            # self.utils.save_object(file_path=file_path,obj=preprocessor)
            self.utils.save_object(preprocessor_path,preprocessor)
            X_train_scaled=preprocessor.fit_transform(X_train)
            X_test_scaled=preprocessor.transform(X_test)
            train_file=pd.concat([pd.DataFrame(X_train_scaled), pd.DataFrame(y_train)], axis=1)
            test_file=pd.concat([pd.DataFrame(X_test_scaled),pd.DataFrame(y_test)],axis=1)
            train_file.to_csv(self.datatransformation.train_data,index=False)
            test_file.to_csv(self.datatransformation.test_data,index=False)
            train_arr = np.c_[X_train_scaled, np.array(y_train)]
            test_arr = np.c_[X_test_scaled, np.array(y_test)]

            logging.info("Exited from data scaling function of Data Tranformation")
            return X_train_scaled,X_test_scaled,y_train,y_test
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def initiate_data_Transfomration(self,file_path):
        logging.info("Entered into the intitaiate_data_Transfomrtaion of Data Tranformation file ")
        try:
            X_train_scaled,X_test_scaled,y_train,y_test=self.Scaling_data(file_path=file_path)
            logging.info("Exited from the intitaiate_data_Transfomrtaion of Data Tranformation file ")
            return X_train_scaled,X_test_scaled,y_train,y_test
        except Exception as e:
            raise CustomException(e,sys) from e
        
        
            
        

            




        

        
        


