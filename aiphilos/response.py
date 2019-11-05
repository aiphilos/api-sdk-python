from enum import Enum, auto


class ResponseType(Enum):
    HEALTH = auto()
    LANGUAGES = auto()
    PARSE_STRING = auto()
    PARSE_STRINGS = auto()


class Response(object):
    def __init__(self, response, response_type):
        self.wrapped_response = response
        self.response_type = response_type

    def type(self):
        return self.response_type

    def status_code(self):
        return self.wrapped_response.status_code

    def raise_for_status(self):
        return self.wrapped_response.raise_for_status()

    def text(self):
        return self.wrapped_response.text

    def encoding(self):
        return self.wrapped_response.encoding

    def json(self):
        return self.wrapped_response.json()
