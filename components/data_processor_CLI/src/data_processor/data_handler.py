# Handles data reading and writing
import pandas as pd

def read_data(filepath):
    return pd.read_csv(filepath)