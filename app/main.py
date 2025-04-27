from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import Field, SQLModel, create_engine, Session, select


# Database engine
sqlite_file_name = "address_book.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


# Create database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# @app.on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


# Data model.
class Contact(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    phone: str
    email: str


# Base route.
@app.get("/")
def index():
    return {"message": "Hello, World!"}


# Route to get all contacts.
@app.get("/contacts")
def get_contacts():
    with Session(engine) as session:
        contacts = session.exec(select(Contact)).all()
        return contacts


# Route to get one contact, by ID.
@app.get("/contacts/{id}")
def get_contact(id: int):
    with Session(engine) as session:
        contact = session.get(Contact, id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        return contact


# Route to create a new contact.
@app.post("/contacts")
def create_contact(new_contact: Contact):
    with Session(engine) as session:
        existing_contact = session.get(Contact, new_contact.email)
        if existing_contact:
            raise HTTPException(status_code=400, detail="Contact already exists.")
        session.add(new_contact)
        session.commit()
        session.refresh(new_contact)
        return new_contact


# Route to update an existing contact.
@app.put("/contacts/{id}")
def update_contact(id: int, updated_contact: Contact):
    with Session(engine) as session:
        existing_contact = session.get(Contact, id)
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
    with Session(engine) as session:
        contact = session.get(Contact, id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        session.delete(contact)
        session.commit()
        return {"message": f"Contact ID: {id} deleted."}
