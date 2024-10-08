from fastapi import APIRouter
from {{cookiecutter.api_module_name}}.meta.api_meta import Health, Version

# Custom APIRouter
router = APIRouter()


@router.get("/health", response_model=Health)
def health(
) -> Health:
    """
    Check the service health.
    """
    return Health(status="UP", message="Service is running")

@router.get("/version", response_model=Version)
def version(
) -> Version:
    """
    Check the service version.
    """
    return Version(number="1.0.0", last_updated="2021-01-01")