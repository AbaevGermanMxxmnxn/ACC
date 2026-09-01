# Requirements Traceability Matrix

| Requirement | Implementation | Verification |
|---|---|---|
| FR-01 | POST /applications | test_create_application |
| FR-02 | Pydantic validation | test_invalid_passport |
| FR-03 | Passport regex | test_invalid_passport |
| FR-04 | CREATED | service.py |
| FR-05 | VERIFICATION | service.py |
| FR-06 | Scoring function | service.py |
| FR-07 | calculate_score() | test_create_application |
| FR-08 | threshold 650 | test_create_application |
| FR-09 | StatusHistory | history endpoint |
| FR-10 | GET application | API endpoint |
| FR-11 | GET history | API endpoint |
| FR-12 | transition map | service.py |
