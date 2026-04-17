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
        df["salary"] = df["salary"].astype(str).str.replace(",", "")
    # Convert salary to numeric (example: remove currency symbols and commas)
    #df['salary'] = df['salary'].replace('[\$,]', '', regex=True).astype(float)
    
    return df