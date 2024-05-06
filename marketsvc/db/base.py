from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine("sqlite+pysqlite:///market.db", echo=True)

class Base(DeclarativeBase):
    pass
