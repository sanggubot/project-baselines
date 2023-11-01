import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the variables as you normally would with os.environ
env_config = {
    "db_user": os.environ.get("DB_USER"),
    "db_password": os.environ.get("DB_PASSWORD"),
    "db_host": os.environ.get("DB_HOST"),
    "db_port": os.environ.get("DB_PORT"),
    "db_name": os.environ.get("DB_NAME"),
    "db_uri": os.environ.get("DB_URI"),
    "db_autogenerate_target_schema": os.environ.get("DB_AUTOGENERATE_TARGET_SCHEMA"),
}