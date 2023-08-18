import os
import sys
import pickle
from src.logger import logging
from src.exception import CustomException
from src.constant import *
from dataclasses import dataclass
sys.path.append("D:\Breast_Cancer_assignment")


@dataclass
class UtilsConfig:
    artifact_folder: str = os.path.join(artifact_folder, "artifacts")


class Mainutils:
    def __init__(self):
        self.file_path = UtilsConfig()

    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_objects method class  Mainutils class ")
        try:
            with open(file_path, "wb") as f:
                pickle.dump(obj, f)
            logging.info('Exited from the save_object of method class of Mainutils class ')
        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def load_object(file_path):
        logging.info('Entered the load objects of the Main utils class ')
        try:
            with open(file_path, 'rb') as f:
                obj = pickle.load(f)
            logging.info("Exited  from the load objects cof the Main utils class")
            return obj
        except Exception as e:
            raise CustomException(e, sys) from e
