# Bank Loan Application Processing System

Учебное web-приложение для портфолио ИТ-аналитика. Система принимает заявку на потребительский кредит, валидирует данные, выполняет учебный скоринг, принимает решение и сохраняет историю статусов.

## Архитектура

Client → REST API → Application Service → PostgreSQL → Scoring Service → Decision

В локальном режиме используется SQLite, чтобы проект запускался без отдельной установки БД. Для PostgreSQL достаточно задать `DATABASE_URL`.

## Статусы

CREATED → VERIFICATION → SCORING → APPROVED / REJECTED → CONTRACT

## Запуск

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
uvicorn src.main:app --reload
```

Swagger: http://127.0.0.1:8000/docs

## Пример запроса

```json
{
  "client_id": "CL-10001",
  "full_name": "Иван Иванов",
  "passport_series": "4510",
  "passport_number": "123456",
  "monthly_income": 150000,
  "requested_amount": 500000,
  "term_months": 24
}
```

## Важно

Скоринговая модель является учебной и не предназначена для реального кредитования. Реальные KYC/AML, БКИ, авторизация и заключение договора в MVP не реализованы.

## Frontend

Добавлен web-интерфейс в стиле **LEX OS / BVS-inspired UX/UI** 

После запуска сервера откройте:

`http://127.0.0.1:8000/`

REST API и Swagger остаются доступны:

`http://127.0.0.1:8000/docs`
