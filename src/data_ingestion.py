import os
from abc import ABC, abstractmethod
import pandas as pd

import zipfile

# define the DataIngestion Interface:

class DataIngestion(ABC):
    @abstractmethod
    def ingest_data(self):
        pass


class ZipDataIngestion(DataIngestion):

    def ingest_data(self, file_path: str) -> pd.DataFrame:
        """
        This method extract the .zip file and return the pandas dataframe.
        
        Args:
            file_path: this is your file path.
        Returns:
            pandas dataframe.
        """

        # checking the format of file is valid or not
        if not file_path.endswith('.zip'):
            raise ValueError("The provided file is not a .zip file.")

        # extact the zip file.
        with zipfile.ZipFile(file_path, 'r') as file:
            file.extractall('extracted_data')
        

        # find the extracted file in this extracted_data folder
        extracted_file = os.listdir('extracted_data')
        extracted_data_file = [data_f for data_f in extracted_file if data_f.endswith('.csv')]

        if len(extracted_data_file) == 0:
            raise FileNotFoundError('No CSV file found in the extracted data.')
        if len(extracted_data_file) > 1:
            raise ValueError('More than one CSV file found in the extracted data.')

        csv_file_path = os.path.join('extracted_data', extracted_data_file[0])
        df = pd.read_csv(csv_file_path)
        return df
        


class DataIngestionFactory:
    @staticmethod
    def get_data_ingestion(file_extention: str):
        if file_extention == '.zip':
            return ZipDataIngestion()
        else:
            raise ValueError("No factory found for the given file type.")

if __name__ == "__main__":
    # file_path = "/Users/rahulprajapati/Documents/GitHub/end-to-end-ml-project/data/archive.zip"
    # file_ext = os.path.splitext(file_path)[1]
    # data_ingestion = DataIngestionFactory.get_data_ingestion(file_ext)
    # df = data_ingestion.ingest_data(file_path)
    # print(df.shape)
    pass