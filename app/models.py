from sqlalchemy import Column, Integer, String, Date, Text
from .database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    url = Column(String(255))
    published_date = Column(Date)
