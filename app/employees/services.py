from sqlmodel import Session, select
from .schemas import EmployeeCreate, Employee, EmployeeWithRole
from app.database.models import Employee as DBEmployee

def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = DBEmployee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session):
    return db.exec(select(Employee)).all()

def update_employee(db: Session):
    return db.exec(select(Employee)).all()

def delete_employee(db: Session):
    return db.exec(select(Employee)).all()

def get_employees_with_roles(db: Session):
    return db.exec(EmployeeWithRole).all()