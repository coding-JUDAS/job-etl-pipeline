from sqlalchemy import create_engine

def get_engine():
    engine = create_engine('sqlite:///jobs.db', echo=True)
    return engine