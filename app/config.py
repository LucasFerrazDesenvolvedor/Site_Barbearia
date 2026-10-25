from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Barbearia Matheus do Corte API"
    DATABASE_URL: str = "sqlite:///./barbearia.db"
    
    WHATSAPP_API_URL: str = ""
    WHATSAPP_TOKEN: str = ""
    ADMIN_WHATSAPP_NUMBER: str = "5583999999999"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()