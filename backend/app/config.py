from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60 * 24

    gemini_api_key: str
    gemini_model: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()