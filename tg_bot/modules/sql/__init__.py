from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI


def start() -> scoped_session:
    if 'sqlite' in DB_URI:
        # SQLite အတွက် client_encoding မပါဘူး
        engine = create_engine(DB_URI)
    else:
        # PostgreSQL အတွက် client_encoding ပါတယ်
        engine = create_engine(DB_URI, client_encoding="utf8")
    
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
