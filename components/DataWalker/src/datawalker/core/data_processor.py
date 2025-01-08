import pandas as pd

class DataProcessor:
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        return data