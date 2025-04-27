from sqlmodel import Field, SQLModel


# Contact model.
class Contact(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    phone: str
    email: str
