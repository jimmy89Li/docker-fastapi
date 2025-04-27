from fastapi import FastAPI, HTTPException
from sqlmodel import Session
from . import database, models, crud


app = FastAPI(lifespan=database.lifespan)


# Base route.
@app.get("/")
def index():
    return {"message": "Hello, World!"}


# Route to get all contacts.
@app.get("/contacts")
def get_contacts():
    contacts = crud.get_contacts()
    return contacts


# Route to get one contact, by ID.
@app.get("/contacts/{id}")
def get_contact(id: int):
    contact = crud.get_contact(id)
    return contact


# Route to create a new contact.
@app.post("/contacts")
def create_contact(new_contact: models.Contact):
    contact = crud.create_contact(new_contact)
    return contact


# Route to update an existing contact.
@app.put("/contacts/{id}")
def update_contact(id: int, updated_contact: models.Contact):
    existing_contact = crud.update_contact(id, updated_contact)
    return existing_contact


# Route to delete an existing contact.
@app.delete("/contacts/{id}")
def delete_contact(id: int):
    delete_contact = crud.delete_contact(id)
    if delete_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return delete_contact
