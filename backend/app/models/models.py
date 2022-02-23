from re import I
from sqlalchemy import Column, Integer, String

from app.db.database import Base

class User(Base):
    __tablename__ = 'score'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    x = Column(Integer, index=True)
    y = Column(Integer, index=True)
    score = Column(Integer)

