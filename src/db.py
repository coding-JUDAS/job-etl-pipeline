from sqlalchemy import create_engine
from config import DB_URL   
def get_engine():
    engine = create_engine(DB_URL, echo=True)
    return engine