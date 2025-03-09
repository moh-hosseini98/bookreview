from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):

    db_async_connection_str : str
    postgres_user : str
    postgres_db : str
    postgres_password: str
    redis_host : str
    redis_port : str
    secret_key : str
    algorithm : str
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")
    
settings = Settings()    