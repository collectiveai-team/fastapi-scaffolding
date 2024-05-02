from fastapi import APIRouter

# Custom APIRouter
router = APIRouter()

def get_api_router() -> APIRouter:
    return router