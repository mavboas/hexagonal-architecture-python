from fastapi import FastAPI
import uvicorn
from src.app.adapters.port_in.controllers.token_controller import router as _router
from src.app.config.load_config import LoadConfig

app = FastAPI()

app.include_router(_router)

config = LoadConfig()

if __name__ == '__main__':
    uvicorn.run(app, host=config.parameters.host, port=config.parameters.port)
