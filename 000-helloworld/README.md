# Hello World

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
```