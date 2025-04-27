from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from . import database, models


app = FastAPI(lifespan=database.lifespan)


# Base route.
@app.get("/")
def index():
    return {"message": "Hello, World!"}


# Route to get all contacts.
@app.get("/contacts")
def get_contacts():
    with Session(database.engine) as session:
        contacts = session.exec(select(models.Contact)).all()
        return contacts


# Route to get one contact, by ID.
@app.get("/contacts/{id}")
def get_contact(id: int):
    with Session(database.engine) as session:
        contact = session.get(models.Contact, id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        return contact


# Route to create a new contact.
@app.post("/contacts")
def create_contact(new_contact: models.Contact):
    with Session(database.engine) as session:
        existing_contact = session.get(models.Contact, new_contact.email)
        if existing_contact:
            raise HTTPException(status_code=400, detail="Contact already exists.")
        session.add(new_contact)
        session.commit()
        session.refresh(new_contact)
        return new_contact


# Route to update an existing contact.
@app.put("/contacts/{id}")
def update_contact(id: int, updated_contact: models.Contact):
    with Session(database.engine) as session:
        existing_contact = session.get(models.Contact, id)
        if not existing_contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        existing_contact.name = updated_contact.name
        existing_contact.phone = updated_contact.phone
        existing_contact.email = updated_contact.email
        session.add(existing_contact)
        session.commit()
        session.refresh(existing_contact)
        return existing_contact


# Route to delete an existing contact.
@app.delete("/contacts/{id}")
def delete_contact(id: int):
    with Session(database.engine) as session:
        contact = session.get(models.Contact, id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        session.delete(contact)
        session.commit()
        return {"message": f"Contact ID: {id} deleted."}
