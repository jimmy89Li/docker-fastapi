from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from . import database, models


# Get all contacts.
def get_contacts():
    with Session(database.engine) as session:
        contacts = session.exec(select(models.Contact)).all()
        return contacts


# Get one contact, by ID.
def get_contact(id: int):
    with Session(database.engine) as session:
        contact = session.get(models.Contact, id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        return contact


# Create a new contact.
def create_contact(new_contact: models.Contact):
    with Session(database.engine) as session:
        existing_contact = session.get(models.Contact, new_contact.email)
        if existing_contact:
            raise HTTPException(status_code=400, detail="Contact already exists.")
        session.add(new_contact)
        session.commit()
        session.refresh(new_contact)
        return new_contact


# Update an existing contact.
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


# Delete an existing contact.
def delete_contact(id: int):
    with Session(database.engine) as session:
        contact = session.get(models.Contact, id)
        if not contact:
            return None
        session.delete(contact)
        session.commit()
        return {"message": f"Contact ID: {id} deleted."}
