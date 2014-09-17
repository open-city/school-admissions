import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from api.app_config import DB_CONN

engine = create_engine(DB_CONN, convert_unicode=True)

session = scoped_session(sessionmaker(bind=engine, 
                                      autocommit=False, 
                                      autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

def init_db():
    import api.models
    Base.metadata.create_all(bind=engine)
