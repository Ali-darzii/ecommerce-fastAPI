import logging

from cores.settings.app_runner import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev FastAPI ecommerce application"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env"
