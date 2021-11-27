from datetime import date

from pydantic import Field

from application.routes.payloads import Payload


class BaseUserPayload(Payload):
    name: str = Field(alias="nome")
    cpf: str = Field(alias="cpf")
    birthday: date = Field(alias="dataNascimento")


class UserPayload(BaseUserPayload):
    id_user: int = Field(alias="idPessoa")


class SearchUserResponse(UserPayload):
    """Response model to endpoint GET /users/{id}"""


class CreateUserRequest(BaseUserPayload):
    """Request model to endpoint POST /users/"""


class CreateUserResponse(UserPayload):
    """Response model to endpoint POST /users/"""
