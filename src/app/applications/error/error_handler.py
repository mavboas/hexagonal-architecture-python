from fastapi import HTTPException
from src.app.config.log_config import logger


class ErrorHandler:
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def error_handler(self):
        logger(level=20, message=f"Error code: {str(self.code)}, message: {self.message}")
        if self.code in [101, 102, 103, 104, 105]:
            raise HTTPException(status_code=401, detail={"code": self.code, "message": self.message})
        else:
            raise HTTPException(status_code=501, detail={"code": self.code, "message": self.message})
