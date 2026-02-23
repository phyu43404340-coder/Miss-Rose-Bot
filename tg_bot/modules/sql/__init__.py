from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI


def start() -> scoped_session:
    # SQLite အတွက် client_encoding မလိုဘူး
    # PostgreSQL အတွက်လည်း client_encoding မထည့်တော့ဘူး (အားလုံးအဆင်ပြေအောင်)
    engine = create_engine(DB_URI)
    
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
