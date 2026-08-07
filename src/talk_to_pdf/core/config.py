from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    project_name: str = "Talk to PDF API"
    version: str = "0.1.0"

     # Using asyncpg driver. Default points to a local postgres instance.
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/talk_to_pdf"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Setting()