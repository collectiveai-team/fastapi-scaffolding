import os
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware

from {{cookiecutter.api_module_name}}.logger import get_logger
from {{cookiecutter.api_module_name}}.endpoints import login, basics, model
from {{cookiecutter.api_module_name}}.auth import get_current_user

logger = get_logger(__name__)


origins = (
    os.getenv("ORIGINS")
    or "http://localhost,http://localhost:80,http://localhost:3000"  # noqa
)

origins = [origin.strip() for origin in origins.split(",")]

logger.info("Running version: 0.0.1")
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
        content={"message": f"Oops! There goes a rainbow..."},
    )


# Basic and login routes

app.include_router(login.router, prefix="/token", tags=["login"])
app.include_router(basics.router, prefix="/basics", tags=["basics"])
app.include_router(model.router, prefix="/predict", tags=["model"], dependencies=[Depends(get_current_user)])


