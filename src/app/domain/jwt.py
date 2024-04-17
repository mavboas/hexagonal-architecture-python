from pydantic import BaseModel


class Jwt(BaseModel):
    client_id: str
    iat: int
    exp: int
    validated: bool
    time_to_expire: str
