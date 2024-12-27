

import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC, abstractmethod
import pandas as pd


# Define Abstract class for Checking Missing Value.

class MissingValueCheck(ABC):

    def analyzer(self, df: pd.DataFrame):
        
        self.analysis_missing_value(df)
        self.visualize_missing_value(df)

    @abstractmethod
    def analysis_missing_value(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def visualize_missing_value(self, df: pd.DataFrame):
        pass


class SimpleMissingValueAnalysis(MissingValueCheck):

    def analysis_missing_value(self, df: pd.DataFrame):
        """
        this method are used to checking the missing value in this given
        dataframe and return the missing value count.

        Args:
            df: dataframe which perform this opertions.
        Return:
            None: 
        """
        print("Missing Value Analysis:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])



    def visualize_missing_value(self, df: pd.DataFrame):
        """
        this method are used to visualize the null value by using heatmap.

        Args:
            df: dataframe which perform this opertions.
        Return:
            None:
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Value Heatmap')
        plt.show()



if __name__ == "__main__":
#     df = pd.read_csv('/Users/rahulprajapati/Documents/GitHub/end-to-end-ml-project/src/extracted_data/AmesHousing.csv')
#     missing_value = SimpleMissingValueAnalysis()
#     missing_value.analysis_missing_value(df)
#     missing_value.visualize_missing_value(df)  # this will display the heatmap of missing value in

    pass
    

     

