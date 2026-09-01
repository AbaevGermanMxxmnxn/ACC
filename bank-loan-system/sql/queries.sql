-- 1. Количество заявок по статусам
SELECT status, COUNT(*) AS applications_count
FROM loan_applications
GROUP BY status
ORDER BY applications_count DESC;

-- 2. Средний score по статусам
SELECT status, ROUND(AVG(score), 2) AS avg_score
FROM loan_applications
WHERE score IS NOT NULL
GROUP BY status;

-- 3. Одобренные заявки
SELECT id, client_id, requested_amount, monthly_income, score
FROM loan_applications
WHERE status = 'APPROVED'
ORDER BY score DESC;

-- 4. История конкретной заявки
SELECT la.id, la.client_id,
       sh.old_status, sh.new_status, sh.changed_at
FROM loan_applications la
JOIN status_history sh
  ON sh.application_id = la.id
WHERE la.id = 1
ORDER BY sh.changed_at;

-- 5. Approval rate
SELECT ROUND(
    100.0 * SUM(
        CASE WHEN status = 'APPROVED' THEN 1 ELSE 0 END
    ) / NULLIF(COUNT(*), 0),
    2
) AS approval_rate_percent
FROM loan_applications;
