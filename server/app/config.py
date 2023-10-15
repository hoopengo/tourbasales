from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    POSTGRES_USER: str = Field()
    POSTGRES_PASSWORD: str = Field()
    POSTGRES_HOST: str = Field()
    POSTGRES_PORT: str = Field()
    POSTGRES_DB: str = Field()

    class Config:
        case_sensitive = False
        env_prefix = ""


config = Config()
