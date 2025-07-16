import os,sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass   # used to create class variables inshort 
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
#  save raw data, input , outdata save for that we are creating dataIngestionConfig

@dataclass                  # to define class variables you have to use __init__ but with the help of dataclass you can directly define them 
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts',"test.csv")
    raw_data_path:str=os.path.join('artifacts',"data.csv")


class DataIngestion:
  
    def __init__(self) -> None:
        self.ingestion_config=DataIngestionConfig()   #the train_test_raw path saved inside variable

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df=pd.read_csv("notebook/data/stud.csv")
            logging.info("read the dataset as dataset done")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  # exit if its there it won't create new one returns the directory portion of a given file path — that is, it strips off the file name (or the last part of the path) and returns the parent directory.
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path)
            test_set.to_csv(self.ingestion_config.test_data_path)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)

            pass
     

if __name__=="__main__":
    obj=DataIngestion()
    # obj.initiate_data_ingestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_tranformation=DataTransformation()
    data_tranformation.initiate_data_transformation(train_data,test_data)
    
    