from sqlmodel import Session, create_engine

DATABASE_URL = "postgresql://your_username:your_password@localhost/your_database"
engine = create_engine(DATABASE_URL)

def get_session() -> Session:
    with Session(engine) as session:
        yield session
