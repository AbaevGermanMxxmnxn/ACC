# Frontend

Интерфейс выполнен в эстетике **LEX OS / BVS-inspired UX/UI** по предоставленному референсу:

- тёплая off-white / grey палитра;
- оранжевые акцентные системные плитки;
- минималистичная типографика;
- полупрозрачные панели;
- крупная модульная tile-сетка;
- верхняя строка поиска;
- боковая навигация;
- нижний системный dock;
- состояние API / system online;
- modal для создания кредитной заявки.

Frontend находится в `src/static/`.

Он взаимодействует с существующим REST API через:
`POST /api/v1/applications`.

## Подключение к FastAPI

В `src/main.py` нужно подключить `StaticFiles` и корневой HTML:

```python
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
def frontend():
    return FileResponse("src/static/index.html")
```
