"""
configuration module of datasets package
"""
from enum import Enum
from pydantic import BaseSettings


class LoggingLevel(str, Enum):
    """
    Allowed log levels for the application
    """

    CRITICAL: str = "CRITICAL"
    ERROR: str = "ERROR"
    WARNING: str = "WARNING"
    INFO: str = "INFO"
    DEBUG: str = "DEBUG"


class LoggingConfig(BaseSettings):
    """
    Logging settings
    """

    level: LoggingLevel = "DEBUG"

    class Config:
        env_prefix = "log_"
        case_sensitive = False


class S3Config(BaseSettings):
    """
    S3 settings
    """

    endpoint: str = "127.0.0.1:9000"
    access_key: str = "minioadmin"
    secret_key: str = "minioadmin"
    secure: bool = False
    datasets_bucket: str = "datasets"

    class Config:
        env_prefix = ""
        case_sensitive = False


class AppSettings(BaseSettings):
    """
    Application settings can be set using environment variables
    """

    s3: S3Config = S3Config()
    logging: LoggingConfig = LoggingConfig()


SETTINGS = AppSettings()
