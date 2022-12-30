import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
# if SQLALCHEMY_DATABASE_URL.startswith('postgres://'):
#     SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://",
#                                                               "postgresql://",
#                                                               1)
# postgres://ehcavjph:Z2Xd0wqgUqIfI5TGJ5Y1YR06nPFDRbbs@floppy.db.elephantsql.com/ehcavjph
SQLALCHEMY_DATABASE_URL = "postgresql://ehcavjph:Z2Xd0wqgUqIfI5TGJ5Y1YR06nPFDRbbs@floppy.db.elephantsql.com/ehcavjph"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


