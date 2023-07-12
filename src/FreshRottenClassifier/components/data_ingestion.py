import os
import requests
import urllib.request as request
from pathlib import Path
import zipfile
import io
from src.FreshRottenClassifier.logger import logging
from src.FreshRottenClassifier.exceptions import CustomException
from src.FreshRottenClassifier.entity.config_entity import *
from src.FreshRottenClassifier.utils.common import get_size


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        
        self.config = config

    def download_file(self):

        if not os.path.exists(self.config.local_data_file):

            session = requests.Session()
            kaggle_username = 'shabbirhussain1699'
            kaggle_password = 'ed40a963479850d53fbf704326317c45'

            session.cookies.set('username', kaggle_username)
            session.cookies.set('password', kaggle_password)

            login_url = 'https://www.kaggle.com/account/login'

            login_payload = {
                    'action': 'login',
                    'username': kaggle_username,
                    'password': kaggle_password
                    }

            session.post(login_url, data=login_payload)

            r = requests.get(self.config.source_URL, stream=True)
            with open(self.config.local_data_file, 'wb') as file:
                for chunk in r.iter_content(chunk_size=128):
                    file.write(chunk)

            logging.info( "downloaded")

        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        """unzip the zip file

        zip_file_apth: str
        Extracts the zip file into data directory

        Function returns None

        """        

        unzip_file_path = self.config.unzip_dir

        os.makedirs(unzip_file_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            zip_ref.extractall(unzip_file_path)