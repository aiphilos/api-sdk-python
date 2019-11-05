from enum import Enum


class Scheme(Enum):
    HTTP = "http"
    HTTPS = "https"
    DEFAULT = HTTPS
