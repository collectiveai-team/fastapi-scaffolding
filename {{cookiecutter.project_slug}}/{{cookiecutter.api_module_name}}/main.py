import os
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware

from {{cookiecutter.api_module_name}}.logger import get_logger
from {{cookiecutter.api_module_name}}.router import get_api_router
from {{cookiecutter.api_module_name}}.endpoints import login, basics, model
from {{cookiecutter.api_module_name}}.auth import get_current_user

logger = get_logger(__name__)


origins = (
    os.getenv("ORIGINS")
    or "http://localhost,http://localhost:80,http://localhost:3000"  # noqa
)

origins = [origin.strip() for origin in origins.split(",")]

logger.info("Running version: 2.0.2")
logger.info(f"Origins: {origins}")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    return HTTPException(
        status_code=500,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


api_router = get_api_router()

### Basic and login routes

api_router.include_router(login.router, tags=["login"])
api_router.include_router(basics.router, prefix="/basics", tags=["basics"])
api_router.include_router(model.router, prefix="/predict", tags=["basics"], dependencies=[Depends(get_current_user)])


