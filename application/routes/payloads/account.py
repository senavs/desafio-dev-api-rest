from datetime import datetime
from decimal import Decimal
from typing import Union

from pydantic import BaseModel, Field

from application.models.account import AccountModel
from application.routes.payloads import Payload


class BaseAccountPayload(Payload):
    id_user: int = Field(alias="idUsuario")
    amount: Decimal = Field(alias="saldo")
    limit: Decimal = Field(alias="limiteSaqueDiario")
    active: bool = Field(alias="ativo")
    id_account_type: int = Field(alias="idTipoConta")
    create_at: datetime = Field(alias="dataCriacao")


class AccountPayload(BaseAccountPayload):
    id_account: int = Field(alias="idConta")


class SearchAccountResponse(AccountPayload):
    """Response model to endpoint GET /accounts/{id}"""


class ListAccountResponse(BaseModel):
    """Response model to endpoint GET /accounts/user/{id}"""

    accounts: list[Union[AccountPayload, AccountModel]]


class CreateAccountRequest(BaseModel):
    """Request model to endpoint POST /accounts/"""

    id_user: int = Field(alias="idUsuario")
    limit: Decimal = Field(alias="limiteSaqueDiario")
    id_account_type: int = Field(alias="idTipoConta")


class CreateAccountResponse(AccountPayload):
    """Response model to endpoint POST /accounts/"""


class UpdateAccountRequest(BaseModel):
    """Request model to endpoint PUT /accounts/"""

    limit: Decimal = Field(alias="limiteSaqueDiario")


class UpdateAccountResponse(AccountPayload):
    """Response model to endpoint PUT /accounts/"""
