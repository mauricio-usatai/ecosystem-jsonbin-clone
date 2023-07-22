import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DYNAMO_TABLE_NAME: str = os.environ.get("DYNAMO_TABLE_NAME", "jsonbin-clone")
    DEPLOYMENT: str = os.environ.get("DEPLOYMENT", "local")
