from pydantic import BaseModel


class ClientCredential(BaseModel):
    grant_type: str
    client_secret: str
    client_id: str
