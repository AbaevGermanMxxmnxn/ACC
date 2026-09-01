INSERT INTO loan_applications
(client_id, full_name, passport_series, passport_number,
 monthly_income, requested_amount, term_months, score, status)
VALUES
('CL-10001', 'Иван Иванов', '4510', '123456',
 150000, 500000, 24, 850, 'APPROVED'),
('CL-10002', 'Пётр Петров', '4520', '654321',
 50000, 700000, 60, 550, 'REJECTED');

INSERT INTO status_history
(application_id, old_status, new_status)
VALUES
(1, NULL, 'CREATED'),
(1, 'CREATED', 'VERIFICATION'),
(1, 'VERIFICATION', 'SCORING'),
(1, 'SCORING', 'APPROVED'),
(2, NULL, 'CREATED'),
(2, 'CREATED', 'VERIFICATION'),
(2, 'VERIFICATION', 'SCORING'),
(2, 'SCORING', 'REJECTED');
