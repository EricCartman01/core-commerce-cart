import os
from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

    def __str__(self) -> str:
        return str.__str__(self)

    @classmethod
    def is_valid(cls) -> bool:
        return os.environ.get("DD_ENV") in list(cls)
