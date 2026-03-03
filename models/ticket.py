from database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Ticket(Base):
    # create table named 'tickets' in the db
    __tablename__ = "tickets" 
    id = Column(...)
    title = Column(...)
    description = Column(...)
    priority = Column(...)
    status = Column(...)
    created_at = Column(...)

