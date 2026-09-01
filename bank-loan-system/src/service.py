from sqlalchemy.orm import Session
from .models import LoanApplication, StatusHistory
from .schemas import ApplicationCreate
from .scoring import calculate_score

CREATED = "CREATED"
VERIFICATION = "VERIFICATION"
SCORING = "SCORING"
APPROVED = "APPROVED"
REJECTED = "REJECTED"
CONTRACT = "CONTRACT"

ALLOWED_TRANSITIONS = {
    CREATED: {VERIFICATION},
    VERIFICATION: {SCORING, REJECTED},
    SCORING: {APPROVED, REJECTED},
    APPROVED: {CONTRACT},
    REJECTED: set(),
    CONTRACT: set(),
}

def change_status(db: Session, app: LoanApplication, new_status: str):
    old_status = app.status

    if new_status not in ALLOWED_TRANSITIONS.get(old_status, set()):
        raise ValueError(
            f"Invalid transition: {old_status} -> {new_status}"
        )

    app.status = new_status
    db.add(StatusHistory(
        application_id=app.id,
        old_status=old_status,
        new_status=new_status
    ))

def create_application(db: Session, data: ApplicationCreate):
    app = LoanApplication(
        **data.model_dump(),
        status=CREATED
    )

    db.add(app)
    db.commit()
    db.refresh(app)

    change_status(db, app, VERIFICATION)
    change_status(db, app, SCORING)

    app.score = calculate_score(
        app.monthly_income,
        app.requested_amount,
        app.term_months
    )

    if app.score >= 650:
        change_status(db, app, APPROVED)
    else:
        change_status(db, app, REJECTED)

    db.commit()
    db.refresh(app)
    return app

def get_history(db: Session, application_id: int):
    return (
        db.query(StatusHistory)
        .filter(StatusHistory.application_id == application_id)
        .order_by(StatusHistory.id)
        .all()
    )
