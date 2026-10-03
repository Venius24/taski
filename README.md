# Taski

Небольшой учебный менеджер задач: Django REST API и React клиент. Локальный API не имеет пользовательских аккаунтов, поэтому запускайте его только в доверенной среде.

## Запуск

Нужны Python 3.9 и Node.js. В первом терминале:

```powershell
cd backend
py -3.9 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python manage.py migrate
.venv\Scripts\python manage.py runserver
```

В Linux/macOS используйте `.venv/bin/python`. Во втором терминале:

```bash
cd frontend
npm ci
npm start
```

Клиент использует proxy на `http://127.0.0.1:8000` и API `/api/tasks/`. Настройки Django читают переменные из `backend/.env.example` из окружения; `.env` сам не загружается. Для внешнего доступа задайте собственный ключ, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS` и ограничьте доступ к API. Необязательная `DJANGO_DB_PATH` задаёт отдельную SQLite базу.

Проверки: в `backend` — `python manage.py check` и `python manage.py test`; в `frontend` — `CI=true npm test -- --watch=false --runInBand` и `npm run build`. Ранее записанный в истории Git ключ при реальном развёртывании надо ротировать и удалить из истории отдельно.
