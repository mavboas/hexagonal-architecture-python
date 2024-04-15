from src.app.config.log_config import logger
from src.app.utils.enums.grant_type_enum import GRANT_TYPE_ENUM
from src.app.applications.error.error_handler import ErrorHandler
from src.app.applications.use_cases.token.token_generate import TokenGenerateUseCase


class TokenGenerateService:
    def __init__(self, grant_type, client_id, client_secret):
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret

    def token_generate(self):
        logger(f"authentication grant type: {self.grant_type}")
        if self.grant_type in GRANT_TYPE_ENUM.VALUES:
            return TokenGenerateUseCase(self.client_id, self.client_secret).execute()
        return ErrorHandler(101, "Invalid authentication method").error_handler()
