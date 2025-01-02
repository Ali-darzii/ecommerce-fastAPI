from functools import lru_cache
from typing import Dict, Type

from cores.settings.app_runner import AppSettings
from cores.settings.base import AppEnvTypes, BaseAppSettings
from cores.settings.development import DevAppSettings
from cores.settings.production import ProdAppSettings
from cores.settings.test import TestAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
