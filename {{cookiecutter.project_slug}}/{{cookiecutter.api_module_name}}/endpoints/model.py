from fastapi import APIRouter
from {{cookiecutter.api_module_name}}.meta.api_meta import ModelInput, ModelOutput

# Custom APIRouter
router = APIRouter()


@router.get("", response_model=ModelOutput)
async def login_for_access_token(
    input: ModelInput,
) -> ModelOutput:
    return ModelInput(prediction="Hello, World!")