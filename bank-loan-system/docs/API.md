# API

## GET /health

Проверка доступности сервиса.

Response:

```json
{"status": "ok"}
```

## POST /api/v1/applications

Создание кредитной заявки.

Request:

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

## GET /api/v1/applications/{application_id}

Получение заявки.

## GET /api/v1/applications/{application_id}/history

Получение истории статусов.

Интерактивная документация OpenAPI доступна по `/docs`.
