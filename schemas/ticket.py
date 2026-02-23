from pydantic import BaseModel
from datetime import datetime
from typing   import Optional

# define the schema for a ticket

# core attributes of a ticket
class BaseTicket(BaseModel):
    title: str
    description: str
    priority: str

# this is controlled by the client
class CreateTicket(BaseTicket):
    pass

class UpdateTicket(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None

# this is controlled by the server & db
class ResponseTicket(BaseTicket):
    id: int
    status: str
    created_at: datetime



