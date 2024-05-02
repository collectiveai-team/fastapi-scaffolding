from pydantic import BaseModel

class Health(BaseModel):
    status: str
    message: str

class Version(BaseModel):
    number: str
    last_updated: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    read_only: bool | None = False


class UserInDB(User):
    hashed_password: str

class ModelInput(BaseModel):
    model: str

class ModelOutput(BaseModel):
    prediction: str