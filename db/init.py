from sqlalchemy import create_engine

from env_config import env_config

engine = create_engine(env_config.get("db_uri", None), echo=True)
connect = engine.connect()
