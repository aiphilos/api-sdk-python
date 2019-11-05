from enum import Enum


class Host(Enum):
    MAIN = "aiphilos.com"
    LOCAL = "aiphilos.local"
    LOCALHOST = "localhost"
    LOCALIP = "127.0.0.1"
    LOCALIP6 = "::1"
    DEFAULT = MAIN
