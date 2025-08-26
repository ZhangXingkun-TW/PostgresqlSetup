Project setup

```bash
pip install -r requirements.txt
docker-compose up -d
```

init alembic

```bash
alembic init migrations
```

change model & automate migration

```bash
alembic revision --autogenerate -m "add email to users"
```

add new migration file for SQL

```bash
alembic revision -m "add check constraint users.name" --empty
```

run migration

```bash
alembic upgrade head
```

downgrade migration

```bash
alembic downgrade -1
```