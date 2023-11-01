<!-- # Python Fastapi Development Environment with DevContainer, Docker, and Poetry

This is a basic Fastapi project setup for a Python development environment using DevContainer, Docker, and Poetry. It includes custom workspace settings for Visual Studio Code (VSCode) with a Black formatter configuration and a maximum line length of 100 characters.


## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>

2. Run .devcontainer in vscode

3. Install Poetry env and use

   ```bash
   poetry install

4. Run Server

   ```bash
   cd app
   uvicorn main:app --reload -->

<!-- DB_USER=supabase_admin
DB_PASSWORD=[]
DB_HOST=[].rds.amazonaws.com
DB_PORT=5432
DB_NAME=postgres
DB_URI=postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
DB_AUTOGENERATE_TARGET_SCHEMA=public -->

<!-- Generic single-database configuration.

alembic history
alembic downgrade -1
alembic upgrade head
alembic revision --autogenerate -m "auto test"
alembic revision -m "init"
alembic check

https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a <- +schema
https://alembic.sqlalchemy.org/en/latest/tutorial.html
https://alembic.sqlalchemy.org/en/latest/autogenerate.html
https://blog.aaronroh.org/115
https://codeac.tistory.com/114 -->