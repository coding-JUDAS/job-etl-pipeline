from db import get_engine

def load_to_db(df):
    engine = get_engine()
    df.to_sql('jobs', con=engine, if_exists='replace', index=False)