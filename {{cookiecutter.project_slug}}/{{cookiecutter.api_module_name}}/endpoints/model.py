from {{cookiecutter.api_module_name}}.router import get_api_router
from {{cookiecutter.api_module_name}}.meta.api_meta import ModelInput, ModelOutput

router = get_api_router()

@router.get("", response_model=ModelOutput)
async def login_for_access_token(
    input: ModelInput,
) -> ModelOutput:
    return ModelInput(prediction="Hello, World!")