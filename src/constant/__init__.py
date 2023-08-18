import os 
import sys 
import pymongo


AWS_S3_BUCKET_NAME='Breast_Cancer_Detection'
MONGODB_URL="mongodb+srv://vikalp026varshney:Vikalp026var@cluster0.r31hq0n.mongodb.net/?retryWrites=true&w=majority"
MONGO_DATABASE_NAME='Breast_cancer'
MONGO_DATABASE_COLLECTION='data'
TARGET_COLUMN='diagnosis'
MODEL_FILE_NAME='model.pkl'
MODEL_FILE_EXTENSION='.pkl'
artifact_folder='artifacts'
filename='predictions'
preprocessor='preprocessor.pkl'
PREDICTION='prediction'
PREDICTION_FILE='prediction.csv'