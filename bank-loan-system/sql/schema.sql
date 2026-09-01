CREATE TABLE loan_applications (
    id SERIAL PRIMARY KEY,
    client_id VARCHAR(50) NOT NULL,
    full_name VARCHAR(200) NOT NULL,
    passport_series VARCHAR(4) NOT NULL,
    passport_number VARCHAR(6) NOT NULL,
    monthly_income NUMERIC(14,2) NOT NULL,
    requested_amount NUMERIC(14,2) NOT NULL,
    term_months INTEGER NOT NULL,
    score INTEGER,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE status_history (
    id SERIAL PRIMARY KEY,
    application_id INTEGER NOT NULL REFERENCES loan_applications(id),
    old_status VARCHAR(30),
    new_status VARCHAR(30) NOT NULL,
    changed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_loan_applications_client_id
ON loan_applications(client_id);

CREATE INDEX idx_status_history_application_id
ON status_history(application_id);
