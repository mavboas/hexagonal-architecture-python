from src.app.utils.dict_to_object import DictToObject


class PayloadDTO:
    def __init__(self, jwt_dict: dict):
        self.jwt_dict = jwt_dict
        self.client_id = self.serialize_jwt_dict().client_id
        self.iat = self.serialize_jwt_dict().iat
        self.exp = self.serialize_jwt_dict().exp

    def serialize_jwt_dict(self):
        return DictToObject(self.jwt_dict)
