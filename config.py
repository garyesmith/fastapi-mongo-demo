"""
Pydantic is used for settings management:
https://pydantic-docs.helpmanual.io/usage/settings/
"""

from pydantic import BaseSettings


class Settings(BaseSettings):

    # app version
    version: str

    # api key
    api_key: str

    # Connection URI for Mongo
    mongo_uri: str

    # Mongo database name
    mongo_dbname: str

    # including this part makes it look in .env to fill the values above:
    class Config:
        env_file = ".env"


settings = Settings()
