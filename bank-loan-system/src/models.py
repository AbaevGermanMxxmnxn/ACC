from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True)
    client_id = Column(String(50), nullable=False, index=True)
    full_name = Column(String(200), nullable=False)
    passport_series = Column(String(4), nullable=False)
    passport_number = Column(String(6), nullable=False)
    monthly_income = Column(Float, nullable=False)
    requested_amount = Column(Float, nullable=False)
    term_months = Column(Integer, nullable=False)
    score = Column(Integer)
    status = Column(String(30), nullable=False)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    history = relationship(
        "StatusHistory",
        back_populates="application",
        cascade="all, delete-orphan"
    )

class StatusHistory(Base):
    __tablename__ = "status_history"

    id = Column(Integer, primary_key=True)
    application_id = Column(
        Integer,
        ForeignKey("loan_applications.id"),
        nullable=False
    )
    old_status = Column(String(30))
    new_status = Column(String(30), nullable=False)
    changed_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    application = relationship(
        "LoanApplication",
        back_populates="history"
    )
