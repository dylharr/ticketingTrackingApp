Packages used:
-- fastapi
-- uvicorn (ASGI server to run FastAPI)
-- sqlalchemy (ORM for database interaction)
-- psycopg2 (Postgres driver)
-- pydantic (for schema definition, automates validation and type enforcement)
-- datetime
-- typing
-- postgresql 

TLDR: An IT ticketing and tracking app is a program that sits on a server and waits for requests. 

REST = structured CRUD over HTTP

browser sends --> "server, give me the tickets"
backend responds --> "here are the tickets"

HTTP methods example:
GET /tickets == read all tickets
GET /tickets/42 == read one ticket
POST /tickets == create new ticket
PUT /tickets/42 == update ticket
DELETE /tickets/42 == delete ticket

Architecture of a ticket:
1. what the database stores (DB model)
2. what the client sends (schema)
3. what the API returns (schema)