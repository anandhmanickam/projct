from sqlmodel import Field, SQLModel, create_engine

DATABASE_URL = "postgresql://your_username:your_password@localhost/your_database"
engine = create_engine(DATABASE_URL)

class Role(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class Employee(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    role_id: int
    dob: str
