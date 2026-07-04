from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Base Config
    ENVIRONMENT: str = "development"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520

    # Frontend
    NEXT_PUBLIC_API_URL: str = "http://localhost:8000/api/v1"

    # Databases
    DATABASE_URL: str
    REDIS_URL: str
    QDRANT_URL: str

    # Agent APIs
    OPENAI_API_KEY: str = ""
    WEATHER_API_KEY: str = ""
    NEWS_API_KEY: str = ""

    # Collectors
    HIRU_NEWS_API_URL: str = "https://api.example.com/hiru"
    ADA_DERANA_RSS_URL: str = "http://adaderana.lk/rss.php"
    NEWSFIRST_RSS_URL: str = "https://www.newsfirst.lk/rss/"

    OPENWEATHER_API_URL: str = "https://api.openweathermap.org/data/2.5/weather"
    OPEN_METEO_API_URL: str = "https://api.open-meteo.com/v1/forecast"

    EXCHANGE_RATE_API_URL: str = "https://api.exchangerate-api.com/v4/latest/USD"
    CBSL_API_URL: str = "https://www.cbsl.gov.lk/api/exchangerates"

    COLLECTOR_TIMEOUT_SECONDS: int = 10
    COLLECTOR_RETRY_COUNT: int = 3
    COLLECTOR_POLLING_INTERVAL_SECONDS: int = 300

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
