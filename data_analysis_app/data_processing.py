import pandas as pd


def load_data(file):
    data = None
    try:
        data = pd.read_csv(file)
    except:
        pass
    return data
