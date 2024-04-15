from pydantic import BaseModel


class Jwt(BaseModel):
    client_id: str
    iat: int
    exp: int
    validate: bool
    time_to_expire: str
