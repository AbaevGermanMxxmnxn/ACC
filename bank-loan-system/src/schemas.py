from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class ApplicationCreate(BaseModel):
    client_id: str = Field(min_length=3, max_length=50)
    full_name: str = Field(min_length=2, max_length=200)
    passport_series: str = Field(pattern=r"^\d{4}$")
    passport_number: str = Field(pattern=r"^\d{6}$")
    monthly_income: float = Field(gt=0)
    requested_amount: float = Field(gt=0)
    term_months: int = Field(gt=0, le=84)

class ApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: str
    full_name: str
    monthly_income: float
    requested_amount: float
    term_months: int
    score: Optional[int]
    status: str
