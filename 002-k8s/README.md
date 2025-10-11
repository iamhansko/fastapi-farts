# To Do App

### Apis
- GET `/tasks`
- POST `/tasks`
- PUT `/tasks/{id}`
- DELETE `/tasks/{id}`
- PUT `/tasks/{id}/done`
- DELETE `/tasks/{id}/done`

### Structure
```
📦todoapp
 ┣ 📂api
 ┃  ┣ 📂cruds
 ┃  ┃ ┣ 📜done.py
 ┃  ┃ ┣ 📜task.py
 ┃  ┃ ┗ 📜__init__.py
 ┃  ┣ 📂models
 ┃  ┃ ┣ 📜task.py
 ┃  ┃ ┗ 📜__init__.py
 ┃  ┣ 📂routers
 ┃  ┃ ┣ 📜done.py
 ┃  ┃ ┣ 📜task.py
 ┃  ┃ ┗ 📜__init__.py
 ┃  ┣ 📂schemas
 ┃  ┃ ┣ 📜done.py
 ┃  ┃ ┣ 📜task.py
 ┃  ┃ ┗ 📜__init__.py
 ┃  ┣ 📜db.py
 ┃  ┣ 📜main.py
 ┃  ┣ 📜migrate_db.py
 ┃  ┗ 📜__init__.py
 ┣ 📂tests
 ┃  ┣ 📜test_main.py
 ┃  ┗ 📜__init__.py
 ┣ 📜.gitignore
 ┣ 📜docker-compose.yaml
 ┣ 📜Dockerfile
 ┣ 📜poetry.lock
 ┣ 📜pyproject.toml
 ┗ 📜README.md
```

### Requirements
- Install Docker or Docker Desktop
- Create `pyproject.toml` (if `pyproject.toml` does not exist)

  ```bash
  docker compose run --entrypoint "poetry init --name fastapi-app --dependency fastapi --dependency uvicorn[standard] --dependency sqlalchemy --dependency aiomysql --dependency pytest --dependency pytest_asyncio --dependency httpx==0.27.2 --dependency aiosqlite" fastapi-app
  ```

### Deployment
```bash
docker compose run --entrypoint "poetry install --no-root" fastapi-app
docker compose up -d
```

### DB Connection
```bash
docker compose exec db mysql demo
```

### DB Migration
```bash
docker compose exec fastapi-app poetry run python -m api.migrate_db
```

### Test
```bash
docker compose run --entrypoint "poetry run pytest" fastapi-app
```

### Package Installation
```bash
docker compose exec fastapi-app poetry add PACKAGE_TO_INSTALL
```

