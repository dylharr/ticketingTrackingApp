Packages used:
-- fastapi
-- uvicorn (ASGI server to run FastAPI)
-- sqlalchemy (ORM for database interaction)
-- psycopg2 (Postgres driver)

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