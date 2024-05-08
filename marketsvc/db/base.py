from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///market.db", echo=True)

class Base(DeclarativeBase):
    pass
