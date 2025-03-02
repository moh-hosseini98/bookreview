from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):

    DB_ASYNC_CONNECTION_STR : str
    postgres_user : str
    postgres_db : str
    postgres_password: str
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")
    
settings = Settings()    