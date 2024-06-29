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
 ┃ ┣ 📂cruds
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂models
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂routers
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂shemas
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜main.py
 ┃ ┗ 📜__init__.py
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
  docker compose run --entrypoint "poetry init --name fastapi-app --dependency fastapi --dependency uvicorn[standard]" fastapi-app
  ```

### Deployment
```bash
docker compose run --entrypoint "poetry install --no-root" fastapi-app
docker compose up -d

# DB Migration
docker compose exec fastapi-app poetry run python -m api.migrate_db
```

### DB Connection
```bash
docker compose up -d
docker compose exec db mysql demo
```

### Package Installation
```bash
docker compose up -d
docker compose exec fastapi-app poetry add PACKAGE_TO_INSTALL
```