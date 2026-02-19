# ticket, user, asset = core resources
from fastapi import FastAPI

app = FastAPI() 


# Read all tickets (GET)
@app.get("/tickets")
def get_tickets():
    return {"operation": "get all tickets"}

# Read specific ticket (GET {id})
@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    return {"operation": f"get ticket {ticket_id}"}

# Create new ticket (POST)
@app.post("/tickets")
def create_ticket():
    return {"operation": "create ticket"}


# Replace ticket (PUT {id})
@app.put("/tickets/{ticket_id}")
def replace_ticket(ticket_id: int):
    return {"operation": f"replace ticket {ticket_id}"}

# Update ticket (PATCH {id})
@app.patch("/tickets/{ticket_id}")
def update_ticket(ticket_id: int):
    return {"operation": f"update ticket {ticket_id}"}

# Delete ticket (DELETE {id})
@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    return {"operation": f"delete ticket {ticket_id}"}