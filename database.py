from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Url_DataBase = "postgresql://yourusername:yourpassword@localhost:5432/yourdatabase"

engine = create_engine(Url_DataBase)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
