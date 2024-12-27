
from abc import ABC, abstractmethod
import pandas as pd
import os



# This is Strategy based class
#-----------------------------
# Define common Interface for data inspection strategy

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        perform specific type of data frame inspection

        Args:
            df: pandas dataframe
        Return:
            None
        """
        pass

# Define Concrete Strategy for Data Type Inspection
class DataTypeInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        print all data type of given columns of datafram.

        Args:
            df: pandas dataframe
        Return:
            None: print the all the data type of columns of given dataframe.
        """
        print(df.info())


# Define Concrete Strategy for summary of dataframe.
class SummaryInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        print summary of dataframe.

        Args:
            df: pandas dataframe for summary inspection.
        Return:
            None: print the summary of data numerical and categorical data type.
        """
        print("\n Summary of Numerical features.")
        print(df.describe())
        print("\n Summary of Categorical features.")
        print(df.describe(include = ['O']))


# Define the Context for DataInspectionStrategy.
class DataInspection:

    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initialize the DataInspection for specific strategy.
        
        Args:
            strategy: the strategy which used of inspection.

        Return:
            None: 
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        self._strategy.inspect(df)


if __name__ == "__main__":
    # df = pd.read_csv('/Users/rahulprajapati/Documents/GitHub/end-to-end-ml-project/src/extracted_data/AmesHousing.csv')
    
    # obj_data = DataInspection(DataTypeInspectionStrategy())
    # obj_data.execute_inspection(df)
    # print('------------------')

    # obj_data.set_strategy(SummaryInspectionStrategy())
    # obj_data.execute_inspection(df)  # execute the inspection strategy.  # noqa:
    pass
    


        
