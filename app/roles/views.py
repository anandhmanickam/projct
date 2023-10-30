from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from sqlalchemy.orm import sessionmaker
from schemas import Role, RoleCreate
from services import create_role, get_roles, update_roles, delete_roles
from database.session import engine

router = APIRouter()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@router.post("/roles/", response_model=Role)
def create_role_api(role: RoleCreate, db: Session = Depends(SessionLocal)):
    return create_role(db, role)

@router.get("/roles/{role_id}", response_model=Role)
def get_role_api(role_id: int, db: Session = Depends(SessionLocal)):
    db_role = get_roles(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.put("/roles/{role_id}", response_model=Role)
def update_role_api(role_id: int, role: RoleCreate, db: Session = Depends(SessionLocal)):
    db_role = update_roles(db, role_id, role)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.delete("/roles/{role_id}", response_model=Role)
def delete_role_api(role_id: int, db: Session = Depends(SessionLocal)):
    db_role = get_roles(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    delete_roles(db, role_id)
    return db_role
