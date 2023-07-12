import sys
from src.FreshRottenClassifier.config.configuration import ConfigurationManager
from src.FreshRottenClassifier.components.data_ingestion import DataIngestion
from src.FreshRottenClassifier.logger import logging
from src.FreshRottenClassifier.exceptions import CustomException

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    try:
        logging.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<")
    except Exception as e:
        raise CustomException(e, sys)    