from db import get_engine
from config import TABLE_NAME

def load_to_db(df):
    engine = get_engine()
    df.to_sql(TABLE_NAME, con=engine, if_exists='replace', index=False)