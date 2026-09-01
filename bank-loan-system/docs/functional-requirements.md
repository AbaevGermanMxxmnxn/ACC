# Functional Requirements

## UC-01 — Submit Loan Application

**Actor:** Client

**Main flow:**

1. Клиент отправляет POST-запрос.
2. API валидирует данные.
3. Создаётся заявка `CREATED`.
4. Заявка переходит в `VERIFICATION`.
5. Заявка переходит в `SCORING`.
6. Scoring Service рассчитывает score.
7. Application Service принимает решение.
8. Система сохраняет результат и историю.
9. API возвращает клиенту результат.

**Alternative flow:**

- Некорректные входные данные → HTTP 422.
- Score ниже порога → `REJECTED`.

## UC-02 — Get Application

1. Клиент передаёт `application_id`.
2. Система ищет заявку.
3. При отсутствии → HTTP 404.
4. При наличии → данные заявки.

## UC-03 — Get Status History

1. Клиент передаёт `application_id`.
2. Система возвращает последовательность изменений статуса.
