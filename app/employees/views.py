from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from sqlalchemy.orm import sessionmaker
from app.database.session import engine
from .services import create_employee, get_employee, update_employee, delete_employee, get_employees_with_roles
from .schemas import EmployeeCreate, Employee, EmployeeWithRole

router = APIRouter()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@router.post("/employees/", response_model=Employee)
def create_employee_api(employee: EmployeeCreate, db: Session = Depends(SessionLocal)):
    return create_employee(db, employee)

@router.get("/employees/{employee_id}", response_model=Employee)
def get_employee_api(employee_id: int, db: Session = Depends(SessionLocal)):
    db_employee = get_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.put("/employees/{employee_id}", response_model=Employee)
def update_employee_api(employee_id: int, employee: EmployeeCreate, db: Session = Depends(SessionLocal)):
    db_employee = update_employee(db, employee_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.delete("/employees/{employee_id}", response_model=Employee)
def delete_employee_api(employee_id: int, db: Session = Depends(SessionLocal)):
    db_employee = get_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    delete_employee(db, employee_id)
    return db_employee

@router.get("/employees/", response_model=list[EmployeeWithRole])
def get_employees_with_roles_api(db: Session = Depends(SessionLocal)):
    return get_employees_with_roles(db)
