import pandas as pd

#Singleton

class DataP:

    __instance = None

    def __init__(self):
        if DataP.__instance is not None:
            raise Exception("Do not create the new object, just get existing (get_instance)")
        else:
            DataP.__instance = self
            pd.set_option('display.max.columns', None)
            pd.set_option('display.width', None)
            pd.set_option('display.max.rows', None)
            self.df = pd.read_csv('../airplanes_data/planes.csv')

            self.df['year'] = self.df['year'].fillna(self.df['year'].mean())
            self.df['year'] = self.df['year'].astype(int)



    @staticmethod
    def get_instance():
        if DataP.__instance is None:
            DataP()
        return DataP.__instance

    def view(self):
        print(self.df)

