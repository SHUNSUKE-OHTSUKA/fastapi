# https://qiita.com/satto_sann/items/4fbc1a4e2b33fa2237d2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

# MYSQL connection information.
# Get the value specified by ConfigMap or Secret.
user_name = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database_name = os.environ['MYSQL_DATABASE']

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

# Create Session.
session = scoped_session(
    # Setting of ORM.
    sessionmaker(
        autocommit=False,
        autoflush=True,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()