import pandas as pd
from config import DATA_PATH

def extract_data():
    df = pd.read_csv(DATA_PATH)
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())