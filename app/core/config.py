from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str

    # .env 파일을 읽어오기 위한 설정
    model_config = SettingsConfigDict(env_file=".env")


# 싱글톤 객체로 생성
settings = Settings()
