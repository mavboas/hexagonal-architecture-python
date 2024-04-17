import hvac
from src.app.config.load_config import LoadConfig



class Vault:
    def __init__(self):
        self.config = LoadConfig()
        self.client = hvac.Client(url=self.config.parameters.vault_url, token=self.config.parameters.vault_token)

    def return_secret(self, secret_key_path):
        return self.client.secrets.kv.read_secret_version(path=secret_key_path)
