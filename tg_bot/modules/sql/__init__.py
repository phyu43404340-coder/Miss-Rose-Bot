from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI


def start() -> scoped_session:
    # Connection pool settings for better performance
    engine = create_engine(
        DB_URI,
        pool_size=5,        # Connection 5 ခုအထိထား
        max_overflow=0,      # Overflow မလုပ်ဘူး (connection 5 ခုပဲသုံးမယ်)
        pool_pre_ping=True   # Connection အလုပ်လုပ်ရဲ့လားစစ်တယ်
    )
    
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
