from src.app.config.log_config import logger
from src.app.applications.use_cases.token.token_validate import TokenValidateUseCase


class TokenValidateService:
    def __init__(self, token):
        self.token = token

    def token_validate(self):
        logger(f"Token to be verified: {self.token}")
        return TokenValidateUseCase(self.token).execute()
