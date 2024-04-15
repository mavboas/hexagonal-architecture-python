from fastapi import APIRouter
from src.app.applications.token_generate_service import TokenGenerateService
from src.app.applications.token_validate_service import TokenValidateService
from src.app.domain.client_credentials import ClientCredential

router = APIRouter()


@router.post("/token", status_code=201)
async def token_generate(client_credential: ClientCredential):
    return TokenGenerateService(grant_type=client_credential.grant_type, client_id=client_credential.client_id,
                                client_secret=client_credential.client_secret).token_generate()


@router.get("/token", status_code=200)
async def token_validate(token: str):
    return TokenValidateService(token=token).token_validate()
