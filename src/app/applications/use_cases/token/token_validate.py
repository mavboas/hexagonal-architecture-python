from src.app.adapters.port_out.vault.vault import Vault
from src.app.config.load_config import LoadConfig
from src.app.applications.use_cases.token.DTO.vault_dto import VaultDTO
from src.app.applications.use_cases.token.DTO.payload_dto import PayloadDTO
from src.app.applications.use_cases.token.DTO.jwt_dto import JwtDTO
from src.app.applications.error.error_handler import ErrorHandler
from src.app.applications.use_cases.token.token_generate import TokenGenerateUseCase
from src.app.domain.jwt import Jwt
import jwt
from src.app.config.log_config import logger




class TokenValidateUseCase:
    def __init__(self, token):
        self.token = token
        self.config = LoadConfig()

    def execute(self):
        _client_id = VaultDTO(Vault().return_secret(self.config.parameters.vault_secret_path)).client_id
        _client_secret = VaultDTO(Vault().return_secret(self.config.parameters.vault_secret_path)).client_secret
        _private_key = VaultDTO(Vault().return_secret(self.config.parameters.vault_secret_path)).private_key
        _public_key = VaultDTO(Vault().return_secret(self.config.parameters.vault_secret_path)).public_key
        return self.validate_jwt(_public_key, _client_id, _client_secret, _private_key)

    def validate_jwt(self, public_key, client_id, client_secret, private_key):
        try:
            jwt_dict = jwt.decode(self.token, public_key, algorithms=['RS256'])
            _client_id = PayloadDTO(jwt_dict).client_id
            _iat = PayloadDTO(jwt_dict).iat
            _exp = PayloadDTO(jwt_dict).exp
            if client_id == _client_id:
                if TokenGenerateUseCase(client_id, client_secret).generate_jwt(private_key, iat=_iat,
                                                                                exp=_exp).access_token == self.token:
                    _jwt = JwtDTO(jwt_dict, True)
                    return Jwt(client_id=_jwt.client_id, iat=_jwt.iat, exp=_jwt.exp, validated=_jwt.validate,
                               time_to_expire=_jwt.time_to_expire)
                else:
                    ErrorHandler(103, "Invalid Token").error_handler()
            else:
                ErrorHandler(103, "Invalid Token").error_handler()

        except jwt.ExpiredSignatureError:
            ErrorHandler(104, "Expired Token").error_handler()
        except jwt.InvalidTokenError:
            ErrorHandler(103, "Invalid Token").error_handler()
        except Exception as e:
            logger(f"Error to validate jwt: {str(e)}")
            ErrorHandler(105, "Was not possible validate the token").error_handler()
