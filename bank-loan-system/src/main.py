from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import LoanApplication
from .schemas import ApplicationCreate, ApplicationResponse
from .service import create_application, get_history

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bank Loan Application Processing System",
    version="1.0.0",
    description="Учебная система обработки кредитных заявок."
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
def frontend():
    return FileResponse("src/static/index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/v1/applications", response_model=ApplicationResponse, status_code=201)
def create_loan_application(data: ApplicationCreate, db: Session = Depends(get_db)):
    return create_application(db, data)

@app.get("/api/v1/applications/{application_id}", response_model=ApplicationResponse)
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = db.get(LoanApplication, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

@app.get("/api/v1/applications/{application_id}/history")
def application_history(application_id: int, db: Session = Depends(get_db)):
    application = db.get(LoanApplication, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return get_history(db, application_id)
