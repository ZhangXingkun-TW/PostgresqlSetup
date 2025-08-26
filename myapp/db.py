import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from alembic import context

config = context.config
db_url = os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url"))
# TODO remove this print after debugging
print('====================================')
print(db_url)
engine = create_engine(db_url, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
