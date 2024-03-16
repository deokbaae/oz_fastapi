import logging

from app.configs.base_settings import Env, Settings

logger = logging.getLogger(__name__)


def get_settings() -> Settings:
    from app.configs.local_settings import LocalSettings

    env = Settings(_env_file=".env", _env_file_encoding="utf-8").ENV
    if env == Env.LOCAL:
        return LocalSettings(_env_file=".env", _env_file_encoding="utf-8")
    logger.warning(f"ENV environment variable is required. current env is {env}")
    return LocalSettings(_env_file=".env", _env_file_encoding="utf-8")


settings = get_settings()
