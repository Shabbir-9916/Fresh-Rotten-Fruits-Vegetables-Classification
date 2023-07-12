import sys
from src.FreshRottenClassifier.logger import logging
from src.FreshRottenClassifier.exceptions import CustomException
from src.FreshRottenClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


except Exception as e:
   raise CustomException(e, sys)
   