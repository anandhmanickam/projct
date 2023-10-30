from sqlmodel import Session, select
from schemas import RoleCreate, Role
from app.database.models import Role as DBRole

def create_role(db: Session, role: RoleCreate):
    db_role = DBRole(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_roles(db: Session):
    return db.exec(select(Role)).all()

def update_roles(db: Session):
    return db.exec(select(Role)).all()

def delete_roles(db: Session):
    return db.exec(select(Role))