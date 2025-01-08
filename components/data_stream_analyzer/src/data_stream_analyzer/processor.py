import pandas as pd

def process_data(stream):
    df = pd.read_csv(stream)
    return df.describe()