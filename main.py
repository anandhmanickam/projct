from fastapi import FastAPI
import uvicorn
from app.employees.views import router as employees_router
from app.roles.views import router as roles_router

app = FastAPI()

app.include_router(employees_router, prefix="/employees")
app.include_router(roles_router, prefix="/roles")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
