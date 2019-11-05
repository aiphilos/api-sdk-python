from enum import Enum


class Route(Enum):
    HEALTH = "health"
    LANGUAGES = "languages"
    SEMANTICS_PARSE_STRING = "semantics/parse"
    SEMANTICS_PARSE_STRINGS = "semantics/parsebatch"
