import unittest
import os.path
import sys
from aiphilos.client import Client
from aiphilos.response import ResponseType

AIPHILOS_PY_SDK_TEST_USER = ""
AIPHILOS_PY_SDK_TEST_KEY = ""


class MainTests(unittest.TestCase):
    def test_health(self):
        client = Client()
        client.set_auth_credentials(AIPHILOS_PY_SDK_TEST_USER, AIPHILOS_PY_SDK_TEST_KEY)
        result = client.get_health()

        self.assertEqual(result.status_code(), 200)
        self.assertEqual(result.type(), ResponseType.HEALTH)
        self.assertTrue("OK" in result.text())

    def test_languages(self):
        client = Client()
        client.set_auth_credentials(AIPHILOS_PY_SDK_TEST_USER, AIPHILOS_PY_SDK_TEST_KEY)
        result = client.get_languages()

        self.assertEqual(result.status_code(), 200)
        self.assertEqual(result.type(), ResponseType.LANGUAGES)
        self.assertTrue("de-de" in result.text())
        self.assertTrue("en-en" in result.text())

    def test_parse_string_ok(self):
        client = Client()
        client.set_auth_credentials(AIPHILOS_PY_SDK_TEST_USER, AIPHILOS_PY_SDK_TEST_KEY)
        result = client.parse_string("Ordner")

        self.assertEqual(result.status_code(), 200)
        self.assertEqual(result.type(), ResponseType.PARSE_STRING)
        self.assertTrue("Schreibware" in result.text())
        self.assertTrue("Verzeichnis" in result.text())
        self.assertTrue("messagecode" in result.json())
        self.assertEqual(result.json()["messagecode"], 0)

    def test_parse_strings(self):
        client = Client()
        client.set_auth_credentials(AIPHILOS_PY_SDK_TEST_USER, AIPHILOS_PY_SDK_TEST_KEY)
        result = client.parse_strings({"example_1": "Ordner leitz", "example_2": "tastatur"})

        self.assertEqual(result.status_code(), 200)
        self.assertTrue("example_1" in result.text())
        self.assertTrue("Schreibware" in result.text())
        self.assertTrue("example_2" in result.text())
        self.assertTrue("Keyboard" in result.text())

    def test_forbidden_without_creds(self):
        client = Client()
        result = client.parse_string("Ordner")

        self.assertEqual(result.status_code(), 401)

    def test_forbidden_invalid_creds(self):
        client = Client()
        client.set_auth_credentials("this-is-an-invalid-user@", "0")
        result = client.parse_string("Ordner")

        self.assertEqual(result.status_code(), 401)


def load_test_config():
    global AIPHILOS_PY_SDK_TEST_USER
    global AIPHILOS_PY_SDK_TEST_KEY

    paths = [os.path.dirname(os.path.realpath(__file__)), "."]
    files = ["test_creds", "test_creds.txt"]

    for p in paths:
        for f in files:
            full = os.path.join(p, f)
            if os.path.exists(full) and os.path.isfile(full):
                with open(full, 'r') as creds:
                    user = creds.readline().strip()
                    if len(user) < 1:
                        continue

                    key = creds.readline().strip()
                    if len(key) < 1:
                        continue

                    AIPHILOS_PY_SDK_TEST_USER = user
                    AIPHILOS_PY_SDK_TEST_KEY = key
                    return True

    return False


if __name__ == '__main__':
    ok = load_test_config()

    if ok:
        unittest.main()
    else:
        hint = ("No API credentials for testing found.\n"
                "Create a text file called 'test_creds.txt',\n"
                "the first line containing the API user name,\n"
                "the second line containing the key you wish to use.")
        print(hint)
        sys.exit(1)
