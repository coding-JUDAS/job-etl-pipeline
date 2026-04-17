def validate_data(df):
    if df.empty:
        raise ValueError("DataFrame is empty.")
    if df.isnull().sum().sum() > 0:
        raise ValueError("Null values detected after cleaning.")
    
    return True