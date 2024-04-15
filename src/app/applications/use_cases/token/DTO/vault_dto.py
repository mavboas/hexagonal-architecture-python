from src.app.utils.dict_to_object import DictToObject
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class VaultDTO:
    def __init__(self, vault_dict: dict):
        self.vault_dict = vault_dict
        self.client_id = self.serialize_vault_dict().client_id
        self.client_secret = self.serialize_vault_dict().client_secret
        self.private_key = serialization.load_pem_private_key(base64.b64decode(self.serialize_vault_dict().private_key),
                                                              password=None,
                                                              backend=default_backend())
        self.public_key = serialization.load_pem_public_key(base64.b64decode(self.serialize_vault_dict().public_key),
                                                            backend=default_backend())

    def serialize_vault_dict(self):
        return DictToObject(self.vault_dict).data.data
