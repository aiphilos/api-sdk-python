import requests
import enum
from aiphilos.environment import Environment
from aiphilos.version import Version
from aiphilos.scheme import Scheme
from aiphilos.host import Host
from aiphilos.language import Language
from aiphilos.route import Route
from aiphilos.response import *

API_SUBDOMAIN = "api"
SEPERATOR_URL_PATH = "/"
SEPERATOR_URL_SUBDOMAIN = "."
SEPERATOR_URL_SCHEME = "://"


class Client(object):
    def __init__(self, auth_user="", auth_key="",
                 default_language=Language.DE_DE,
                 default_environment=Environment.DEFAULT,
                 default_version=Version.DEFAULT,
                 default_scheme=Scheme.DEFAULT,
                 default_host=Host.DEFAULT):
        self.invalidate_cache()

        # Clear defaults
        self.auth_user = ""
        self.auth_key = ""
        self.default_language = ""
        self.default_environment = ""
        self.default_version = ""
        self.default_scheme = ""
        self.default_host = ""
        self.cached_base_url = ""
        self.cached_base_url_with_language = ""

        # Set from params
        self.set_auth_credentials(auth_user, auth_key)
        self.set_default_language(default_language)
        self.set_default_environment(default_environment)
        self.set_default_version(default_version)
        self.set_default_scheme(default_scheme)
        self.set_default_host(default_host)

    def set_auth_credentials(self, user, key):
        self.invalidate_cache()
        self.set_auth_user(user)
        self.set_auth_key(key)

    def set_auth_user(self, user):
        self.invalidate_cache()
        self.auth_user = user

    def set_auth_key(self, key):
        self.invalidate_cache()
        self.auth_key = key

    def set_default_language(self, language):
        self.invalidate_cache()
        self.default_language = language

    def set_default_environment(self, environment):
        self.invalidate_cache()
        self.default_environment = environment

    def set_default_version(self, version):
        self.invalidate_cache()
        self.default_version = version

    def set_default_scheme(self, scheme):
        self.invalidate_cache()
        self.default_scheme = scheme

    def set_default_host(self, host):
        self.invalidate_cache()
        self.default_host = host

    def build_base_url(self):
        url = self.default_scheme.value + SEPERATOR_URL_SCHEME + API_SUBDOMAIN + SEPERATOR_URL_SUBDOMAIN
        if len(enum_value(self.default_environment)) > 0:
            url += enum_value(self.default_environment) + SEPERATOR_URL_SUBDOMAIN
        url += enum_value(self.default_host) + SEPERATOR_URL_PATH
        if len(enum_value(self.default_version)) > 0:
            url += enum_value(self.default_version) + SEPERATOR_URL_PATH

        return url

    def build_base_url_with_language(self):
        url = self.build_base_url()

        if len(enum_value(self.default_language)) > 0:
            url += enum_value(self.default_language) + SEPERATOR_URL_PATH

        return url

    def get_base_url(self):
        if len(self.cached_base_url) < 1:
            self.cached_base_url = self.build_base_url()

        return self.cached_base_url

    def get_base_url_with_language(self):
        if len(self.cached_base_url_with_language) < 1:
            self.cached_base_url_with_language = self.build_base_url_with_language()

        return self.cached_base_url_with_language

    def get_auth(self):
        return self.auth_user, self.auth_key

    def invalidate_cache(self):
        self.cached_base_url = ""
        self.cached_base_url_with_language = ""

    def get_health(self):
        r = requests.get(self.get_base_url() + enum_value(Route.HEALTH), auth=self.get_auth())
        return Response(r, ResponseType.HEALTH)

    def get_languages(self):
        r = requests.get(self.get_base_url() + enum_value(Route.LANGUAGES), auth=self.get_auth())
        return Response(r, ResponseType.LANGUAGES)

    def parse_string(self, string):
        r = requests.get(self.get_base_url_with_language() + enum_value(Route.SEMANTICS_PARSE_STRING),
                         auth=self.get_auth(), params={"query": str(string)})
        return Response(r, ResponseType.PARSE_STRING)

    def parse_strings(self, strings):
        data = []
        for k in strings:
            data.append({"id": k, "query": strings[k]})

        r = requests.post(self.get_base_url_with_language() + enum_value(Route.SEMANTICS_PARSE_STRINGS),
                          auth=self.get_auth(), json={"queries": data})
        return Response(r, ResponseType.PARSE_STRINGS)


def enum_value(v):
    if issubclass(v.__class__, enum.Enum):
        return v.value

    return str(v)