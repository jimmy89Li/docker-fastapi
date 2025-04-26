from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# In-memory database.
address_book = {}


# Data model.
class Contact(BaseModel):
    phone: str
    email: str


# Base route.
@app.get("/")
def index():
    return {"message": "Hello, World!"}


# Route to get all contacts.
@app.get("/contacts")
def get_contacts():
    return address_book


# Route to get one contact, by name.
@app.get("/contacts/{name}")
def get_contact(name: str):
    contact = address_book.get(name)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return contact


# Route to create a new contact.
@app.post("/contacts")
def create_contact(name: str, contact: Contact):
    if name in address_book:
        raise HTTPException(status_code=400, detail="Contact already exists.")
    address_book[name] = contact
    return {"message": f"Contact {name} added to the address book."}


# Route to update an existing contact.
@app.put("/contacts/{name}")
def update_contact(name: str, contact: Contact):
    if name not in address_book:
        raise HTTPException(status_code=404, detail="Contact not found.")
    address_book[name] = contact
    return {"message": f"Contact {name} updated."}


# Route to delete an existing contact.
@app.delete("/contacts/{name}")
def delete_contact(name: str):
    if name not in address_book:
        raise HTTPException(status_code=404, detail="Contact not found.")
    address_book.pop(name)
    return {"message": f"Contact {name} removed from address book."}
