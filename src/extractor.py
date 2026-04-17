import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = extract_data("./data/jobs_raw.csv")
    print(df.head())