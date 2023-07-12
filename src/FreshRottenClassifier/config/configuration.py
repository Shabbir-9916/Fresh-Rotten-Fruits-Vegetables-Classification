from src.FreshRottenClassifier.constants import *
from src.FreshRottenClassifier.utils.common import read_yaml, create_directories
from src.FreshRottenClassifier.entity.config_entity import *
import sys
from src.FreshRottenClassifier.logger import logging
from src.FreshRottenClassifier.exceptions import CustomException

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)


        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:

        try:
            config = self.config.data_ingestion

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )

            return data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)