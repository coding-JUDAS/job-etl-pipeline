import pandas as pd

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values (example: fill with 'Unknown')
    df = df.dropna()
    
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Example: clean salary column if exists
    if "salary" in df.columns:
        df["salary"] = (
            df["salary"]
            .astype(str)
            .str.replace(",", "")
            .str.extract(r"(\d+)")
            .astype(float)
        )

    if "job_title" in df.columns:
        df["job_title"] = df["job_title"].str.lower().str.strip()
    
    return df