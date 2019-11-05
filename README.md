# aiPhilos API Python SDK

Python SDK for the aiPhilos API.

See [aiphilos.com](https://aiphilos.com). Docs on [docs.aiphilos.com](https://docs.aiphilos.com).

## Usage
#### Creating and configuring the client
```python
from aiphilos.client import Client
from aiphilos.language import Language

# Create client
client = Client()

# Configure client
client.set_auth_credentials("user", "pass")
client.set_default_language(Language.DE_DE)

# Use client
```

#### Parsing a single string
```python
from aiphilos.client import Client

client = Client("user", "pass")

result = client.parse_string("Ordner")
```

#### Parsing multiple strings
```python
from aiphilos.client import Client

client = Client("user", "pass")

result = client.parse_strings({"example_1": "Ordner leitz", "example_2": "tastatur"})
```

## License
This library is available under the Apache 2.0 License.

## Contact
Want to get in touch? Contact: [aiphilos.com](https://aiphilos.com/kontakt/).