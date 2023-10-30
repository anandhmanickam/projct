from sqlmodel import SQLModel, Field

class Employee(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    role_id: int
    dob: str
