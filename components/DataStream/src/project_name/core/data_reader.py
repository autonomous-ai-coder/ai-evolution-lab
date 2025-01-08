import pandas as pd

class DataReader:
    def __init__(self, source):
        self.source = source
        
    def read(self):
        return pd.read_csv(self.source)