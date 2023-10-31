from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users_details"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    email = Column(String)

def init_db(engine):
    Base.metadata.create_all(bind=engine)