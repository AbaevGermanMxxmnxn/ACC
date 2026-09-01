import os
os.environ["DATABASE_URL"] = "sqlite:///./test_loan_app.db"

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_create_application():
    payload = {
        "client_id": "CL-TEST",
        "full_name": "Test Client",
        "passport_series": "1234",
        "passport_number": "123456",
        "monthly_income": 150000,
        "requested_amount": 500000,
        "term_months": 24
    }

    response = client.post(
        "/api/v1/applications",
        json=payload
    )

    assert response.status_code == 201
    data = response.json()

    assert data["status"] == "APPROVED"
    assert data["score"] >= 650

def test_invalid_passport():
    payload = {
        "client_id": "CL-TEST-2",
        "full_name": "Test Client",
        "passport_series": "12",
        "passport_number": "123456",
        "monthly_income": 100000,
        "requested_amount": 300000,
        "term_months": 24
    }

    response = client.post(
        "/api/v1/applications",
        json=payload
    )

    assert response.status_code == 422
