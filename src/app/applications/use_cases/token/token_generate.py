from src.app.adapters.port_out.vault.vault import Vault
from src.app.config.load_config import LoadConfig
from src.app.applications.use_cases.token.DTO.vault_dto import VaultDTO
from src.app.applications.error.error_handler import ErrorHandler
from src.app.domain.token import Token
import jwt
from datetime import datetime, timedelta

config = LoadConfig()


class TokenGenerateUseCase:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def execute(self):
        _client_id = VaultDTO(Vault().return_secret(config.parameters.vault_secret_path)).client_id
        _client_secret = VaultDTO(Vault().return_secret(config.parameters.vault_secret_path)).client_secret
        _private_key = VaultDTO(Vault().return_secret(config.parameters.vault_secret_path)).private_key
        if self.client_id == _client_id and self.client_secret == _client_secret:
            return self.generate_jwt(_private_key)
        else:
            ErrorHandler(102, "Invalid credentials").error_handler()

    def generate_jwt(self, private_key, iat=None, exp=None):
        if iat is None:
            iat = datetime.utcnow()
        if exp is None:
            exp = datetime.utcnow() + timedelta(seconds=config.parameters.token_expiration_time)
        payload = {
            "sub": self.client_id,
            "client_id": self.client_id,
            'iat': iat,
            'exp': exp
        }
        return Token(access_token=jwt.encode(payload, private_key, algorithm="RS256"),
                     token_type="Bearer",
                     expires_in=config.parameters.token_expiration_time,
                     refresh_token=jwt.encode(payload, private_key, algorithm="RS256")
                     )
