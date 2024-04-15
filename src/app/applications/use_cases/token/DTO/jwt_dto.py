from src.app.utils.dict_to_object import DictToObject
from datetime import datetime


class JwtDTO:
    def __init__(self, jwt_dict: dict, validate: bool):
        self.jwt_dict = jwt_dict
        self.client_id = self.serialize_jwt_dict().client_id
        self.iat = self.serialize_jwt_dict().iat
        self.exp = self.serialize_jwt_dict().exp
        self.validate = validate
        self.time_to_expire = self.calculate_time_to_expire()

    def serialize_jwt_dict(self):
        return DictToObject(self.jwt_dict)

    def calculate_time_to_expire(self):
        return str(datetime.utcfromtimestamp(self.exp) - datetime.utcnow())
