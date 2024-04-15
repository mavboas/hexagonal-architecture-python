import hvac
from src.app.config.load_config import LoadConfig

config = LoadConfig()


class Vault:
    def __init__(self):
        self.client = hvac.Client(url=config.parameters.vault_url, token=config.parameters.vault_token)

    def return_secret(self, secret_key_path):
        return self.client.secrets.kv.read_secret_version(path=secret_key_path)
